from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import ImageModel
from .serializers import ImageModelSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET'])
def retrieve_images_by_tags(request):
    # tags from query parameters
    tags = request.GET.get('tags', '').split(',')
    tags = [tag.strip().lower() for tag in tags if tag.strip()]
    
    # Retrieve pagination parameters
    page_no = int(request.GET.get('page', 1))
    offset = int(request.GET.get('offset', 20))
    start = (page_no - 1) * offset
    end = start + offset + 1  # Fetch one extra to check if there's a next page
    
    # Build the query based on tags
    if not tags:
        images = ImageModel.objects.all()
    else:
        tag_query = Q()
        for tag in tags:
            tag_query |= Q(tags__icontains=tag)
        images = ImageModel.objects.filter(tag_query).distinct()
    
    # Apply pagination
    paginated_images = images[start:end]
    
    # Check if there is a next page
    next_page_exists = len(paginated_images) > offset
    
    # Trim the extra item if it exists
    paginated_images = paginated_images[:offset]
    
    serializer = ImageModelSerializer(paginated_images, many=True)
    response = {
        "pagination": {
            "pageNo": page_no,
            "offset": offset,
            "nextPageExists": next_page_exists,
            "start":start,
            "end":end
        },
        "data": serializer.data
    }
    
    return Response(response)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def createImage(request):
    serializer = ImageModelSerializer(data=request.data)
    if serializer.is_valid():
        image_object = serializer.save()
        return Response(ImageModelSerializer(image_object).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
