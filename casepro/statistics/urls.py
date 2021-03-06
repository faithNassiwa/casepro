from __future__ import unicode_literals

from django.conf.urls import url

from .views import IncomingPerDayChart, RepliesPerMonthChart, MostUsedLabelsChart, DailyCountExportCRUDL

urlpatterns = DailyCountExportCRUDL().as_urlpatterns()

urlpatterns += [
    url(r'^incoming_chart/$', IncomingPerDayChart.as_view(), name='statistics.incoming_chart'),
    url(r'^replies_chart/$', RepliesPerMonthChart.as_view(), name='statistics.replies_chart'),
    url(r'^labels_pie_chart/$', MostUsedLabelsChart.as_view(), name='statistics.labels_pie_chart'),
]
