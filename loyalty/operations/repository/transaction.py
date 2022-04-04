from operations.serializers import TransactionsSerializer


def save(data):
    serializer = TransactionsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return "Error for create"
