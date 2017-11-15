from apps.models import OperationLog
from django.db.models.aggregates import Count

msgS = OperationLog.objects.values_list('admin_name').annotate(Count('id'))
print msgS