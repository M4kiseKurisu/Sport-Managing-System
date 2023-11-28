"""
场地和活动联系
"""
from datetime import datetime

from django.db.models import Q

from api.models import Field
from api.models import Activity
from api.models import ActivityUseField


def check_relation(fid, start_time, end_time):
    """ 检查时段是否合规 """
    field = Field.objects.get(fid=fid)
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    if field.open_time > start_time.time() or field.close_time < end_time.time():
        return False
    overlap_records = ActivityUseField.objects.filter(
        Q(fid=field) &
        (
                Q(start_time__range=(start_time, end_time)) |
                Q(end_time__range=(start_time, end_time)) |
                Q(start_time__lte=start_time, end_time__gte=end_time)
        )
    )
    if overlap_records.exists():
        return False
    else:
        return True


def add_relation(aid, fid, start_time, end_time):
    """ 增加活动使用场地信息 """
    activity = Activity.objects.get(aid=aid)
    field = Field.objects.get(fid=fid)
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    rec = ActivityUseField(aid=activity, fid=field, start_time=start_time, end_time=end_time)
    rec.save()
