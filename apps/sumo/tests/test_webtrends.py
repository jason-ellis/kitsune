from datetime import date

from mock import patch
from nose.tools import eq_

from sumo.tests import TestCase
from sumo.webtrends import Webtrends


KEY_METRICS_JSON_RESPONSE = '{ "definition" : { "accountID" : 123 , "profileID" : "ABC123" , "ID" : "ProfileMetrics" , "name" : "Profile Metrics" , "description" : "" , "language" : null , "timezone" : "UTC -1" , "dimensions" : [ { "ID" : "Profile ID" , "name" : "Profile ID" } ] , "measures" : [ { "name" : "PageViews" , "ID" : "PageViews" , "columnID" : 0 , "measureFormatType" : null },{ "name" : "Visits" , "ID" : "Visits" , "columnID" : 1 , "measureFormatType" : null },{ "name" : "Visitors" , "ID" : "Visitors" , "columnID" : 2 , "measureFormatType" : null },{ "name" : "NewVisitors" , "ID" : "NewVisitors" , "columnID" : 6 , "measureFormatType" : null },{ "name" : "BounceRate" , "ID" : "BounceRate" , "columnID" : 9 , "measureFormatType" : "percent" },{ "name" : "AvgTimeonSite" , "ID" : "AvgTimeOnSite" , "columnID" : 10 , "measureFormatType" : "time_seconds" },{ "name" : "AvgVisitorsperDay" , "ID" : "AvgVisitorsPerDay" , "columnID" : 11 , "measureFormatType" : null },{ "name" : "PageViewsperVisit" , "ID" : "PageViewsPerVisit" , "columnID" : 12 , "measureFormatType" : null },{ "name" : "AvgTimeonSiteperVisitor" , "ID" : "AvgSiteTimePerVisitor" , "columnID" : 13 , "measureFormatType" : "time_seconds" } ] } ,"data" : [ { "ABC123" : {  "attributes" : {  } , "measures" : { "PageViews" : 10523913 , "Visits" : 4274456 , "Visitors" : 4044284 , "NewVisitors" : 2078406 , "BounceRate" : 65.4970831375969 , "AvgTimeonSite" : 274.68279239068 , "AvgVisitorsperDay" : 577754.857142857 , "PageViewsperVisit" : 2.46204733421048 , "AvgTimeonSiteperVisitor" : 96.5800146577243 } , "SubRows" : [  { "period" : "Day" , "start_date" : "2012-01-01" , "end_date" : "2012-01-01" , "measures" : { "PageViews" : 1258143 , "Visits" : 524606 , "Visitors" : 495974 , "NewVisitors" : 254034 , "BounceRate" : 63.9746781394037 , "AvgTimeonSite" : 276.706781356731 , "AvgVisitorsperDay" : 495974 , "PageViewsperVisit" : 2.39826269619486 , "AvgTimeonSiteperVisitor" : 97.029864468702 } , "SubRows" : null }  , {  "period" : "Day" , "start_date" : "2012-01-02" , "end_date" : "2012-01-02" , "measures" : { "PageViews" : 1576014 , "Visits" : 649237 , "Visitors" : 614465 , "NewVisitors" : 320101 , "BounceRate" : 65.3790526417934 , "AvgTimeonSite" : 275.88984425623 , "AvgVisitorsperDay" : 614465 , "PageViewsperVisit" : 2.427486418673 , "AvgTimeonSiteperVisitor" : 97.7010993303117 } , "SubRows" : null }  , {  "period" : "Day" , "start_date" : "2012-01-03" , "end_date" : "2012-01-03" , "measures" : { "PageViews" : 1628215 , "Visits" : 664809 , "Visitors" : 629484 , "NewVisitors" : 326187 , "BounceRate" : 65.9521757376931 , "AvgTimeonSite" : 274.289682249817 , "AvgVisitorsperDay" : 629484 , "PageViewsperVisit" : 2.44914704824995 , "AvgTimeonSiteperVisitor" : 95.4439064376537 } , "SubRows" : null }  , {  "period" : "Day" , "start_date" : "2012-01-04" , "end_date" : "2012-01-04" , "measures" : { "PageViews" : 1622072 , "Visits" : 648066 , "Visitors" : 613411 , "NewVisitors" : 315226 , "BounceRate" : 65.8422136017011 , "AvgTimeonSite" : 272.315030946065 , "AvgVisitorsperDay" : 613411 , "PageViewsperVisit" : 2.50294260152515 , "AvgTimeonSiteperVisitor" : 95.3973388152478 } , "SubRows" : null }  , {  "period" : "Day" , "start_date" : "2012-01-05" , "end_date" : "2012-01-05" , "measures" : { "PageViews" : 1561292 , "Visits" : 619564 , "Visitors" : 585760 , "NewVisitors" : 298016 , "BounceRate" : 65.9460523852257 , "AvgTimeonSite" : 274.38456436392 , "AvgVisitorsperDay" : 585760 , "PageViewsperVisit" : 2.51998502172495 , "AvgTimeonSiteperVisitor" : 96.0481818492215 } , "SubRows" : null }  , {  "period" : "Day" , "start_date" : "2012-01-06" , "end_date" : "2012-01-06" , "measures" : { "PageViews" : 1520252 , "Visits" : 608327 , "Visitors" : 575889 , "NewVisitors" : 294054 , "BounceRate" : 65.7352049144621 , "AvgTimeonSite" : 271.518740910547 , "AvgVisitorsperDay" : 575889 , "PageViewsperVisit" : 2.49907040128089 , "AvgTimeonSiteperVisitor" : 95.6368657848995 } , "SubRows" : null }  , {  "period" : "Day" , "start_date" : "2012-01-07" , "end_date" : "2012-01-07" , "measures" : { "PageViews" : 1357925 , "Visits" : 559847 , "Visitors" : 529301 , "NewVisitors" : 270788 , "BounceRate" : 65.3650015093409 , "AvgTimeonSite" : 278.304308416466 , "AvgVisitorsperDay" : 529301 , "PageViewsperVisit" : 2.42552876053636 , "AvgTimeonSiteperVisitor" : 99.1935042631697 } , "SubRows" : null }  ] } } ] }'
L10N_METRICS_JSON_RESPONSE = '{"definition":{"accountID":123,"profileID":"ABC123","ID":"FRnJo3T7MM6","name":"Directories","language":null,"isRealtime":false,"type":"dimensional","properties":{"isHierarchy":false,"intervalsEnabled":true,"IsSearchable":true,"internalID":"topdirectory_v","IsRealTimeCompatible":true,"ProfileCategory":null,"totals":"all","ContainsRealtimeData":false,"LastUpdate":"03/12/2012 10:22:38","datasource":"engine","enginesearchtime":"5196.3129"},"dimension":{"ID":"Time","name":"Time","type":"period","Range":{"startperiod":"current_day-30","endperiod":"current_day-1"},"Properties":null,"SubDimension":{"ID":"Desc","name":"Path To Directory","type":"data","Range":null,"Properties":null,"SubDimension":null}},"measures":[{"name":"Visits","accumulationType":null,"ID":"Users-0","columnID":0,"measureFormatType":null,"AllowTotals":true,"Sortable":false},{"name":"Hits","accumulationType":null,"ID":"Hits-0","columnID":0,"measureFormatType":null,"AllowTotals":true,"Sortable":false}]},"data":{"02/11/2012-03/11/2012":{"Attributes":null,"measures":{"Visits":null,"Hits":26080500.0},"SubRows":{"http://support.mozilla.org/en-US":{"Attributes":null,"measures":{"Visits":7560328.0,"Hits":14805761.0},"SubRows":null},"http://support.mozilla.org/de":{"Attributes":null,"measures":{"Visits":1262203.0,"Hits":2565829.0},"SubRows":null},"http://support.mozilla.org/es":{"Attributes":null,"measures":{"Visits":815364.0,"Hits":1389487.0},"SubRows":null},"http://support.mozilla.org/ru":{"Attributes":null,"measures":{"Visits":767704.0,"Hits":1304665.0},"SubRows":null},"http://support.mozilla.org/fr":{"Attributes":null,"measures":{"Visits":622241.0,"Hits":1205207.0},"SubRows":null},"http://support.mozilla.org/pt-BR":{"Attributes":null,"measures":{"Visits":364578.0,"Hits":586435.0},"SubRows":null},"http://support.mozilla.org/ja":{"Attributes":null,"measures":{"Visits":326098.0,"Hits":660195.0},"SubRows":null},"http://support.mozilla.org/it":{"Attributes":null,"measures":{"Visits":286096.0,"Hits":551362.0},"SubRows":null},"http://support.mozilla.org/pl":{"Attributes":null,"measures":{"Visits":265332.0,"Hits":452602.0},"SubRows":null},"http://support.mozilla.org/nl":{"Attributes":null,"measures":{"Visits":147086.0,"Hits":300047.0},"SubRows":null},"http://support.mozilla.org/zh-CN":{"Attributes":null,"measures":{"Visits":128521.0,"Hits":233791.0},"SubRows":null},"http://support.mozilla.org/tr":{"Attributes":null,"measures":{"Visits":123517.0,"Hits":197992.0},"SubRows":null},"http://support.mozilla.org/ar":{"Attributes":null,"measures":{"Visits":113500.0,"Hits":188200.0},"SubRows":null},"http://support.mozilla.org/vi":{"Attributes":null,"measures":{"Visits":99362.0,"Hits":149590.0},"SubRows":null},"http://support.mozilla.org/cs":{"Attributes":null,"measures":{"Visits":97591.0,"Hits":180366.0},"SubRows":null},"http://support.mozilla.org/zh-TW":{"Attributes":null,"measures":{"Visits":82061.0,"Hits":129387.0},"SubRows":null},"http://support.mozilla.org/hu":{"Attributes":null,"measures":{"Visits":72521.0,"Hits":122765.0},"SubRows":null},"http://support.mozilla.org/id":{"Attributes":null,"measures":{"Visits":71279.0,"Hits":115014.0},"SubRows":null},"http://support.mozilla.org/sv":{"Attributes":null,"measures":{"Visits":54915.0,"Hits":101559.0},"SubRows":null},"http://support.mozilla.org/th":{"Attributes":null,"measures":{"Visits":49948.0,"Hits":87522.0},"SubRows":null},"http://support.mozilla.org/el":{"Attributes":null,"measures":{"Visits":49460.0,"Hits":74599.0},"SubRows":null},"http://support.mozilla.org/fi":{"Attributes":null,"measures":{"Visits":48009.0,"Hits":90394.0},"SubRows":null},"http://support.mozilla.org/ro":{"Attributes":null,"measures":{"Visits":41807.0,"Hits":70920.0},"SubRows":null},"http://support.mozilla.org/pt-PT":{"Attributes":null,"measures":{"Visits":35553.0,"Hits":61832.0},"SubRows":null},"http://support.mozilla.org/bg":{"Attributes":null,"measures":{"Visits":33361.0,"Hits":53711.0},"SubRows":null},"http://support.mozilla.org/sk":{"Attributes":null,"measures":{"Visits":26417.0,"Hits":44013.0},"SubRows":null},"http://support.mozilla.org/hr":{"Attributes":null,"measures":{"Visits":22480.0,"Hits":37582.0},"SubRows":null},"http://support.mozilla.org/da":{"Attributes":null,"measures":{"Visits":20614.0,"Hits":35557.0},"SubRows":null},"http://support.mozilla.org/ko":{"Attributes":null,"measures":{"Visits":16626.0,"Hits":30233.0},"SubRows":null},"http://support.mozilla.org/lt":{"Attributes":null,"measures":{"Visits":16390.0,"Hits":22904.0},"SubRows":null},"http://support.mozilla.org/nb-NO":{"Attributes":null,"measures":{"Visits":16342.0,"Hits":26377.0},"SubRows":null},"http://support.mozilla.org/sl":{"Attributes":null,"measures":{"Visits":15086.0,"Hits":30286.0},"SubRows":null},"http://support.mozilla.org/uk":{"Attributes":null,"measures":{"Visits":14178.0,"Hits":21741.0},"SubRows":null},"http://support.mozilla.org/fa":{"Attributes":null,"measures":{"Visits":13102.0,"Hits":23856.0},"SubRows":null},"http://support.mozilla.org/sr-CYRL":{"Attributes":null,"measures":{"Visits":11196.0,"Hits":21241.0},"SubRows":null},"http://support.mozilla.org/ca":{"Attributes":null,"measures":{"Visits":8480.0,"Hits":13456.0},"SubRows":null},"http://support.mozilla.org/he":{"Attributes":null,"measures":{"Visits":7924.0,"Hits":14332.0},"SubRows":null},"http://support.mozilla.org/et":{"Attributes":null,"measures":{"Visits":5995.0,"Hits":10088.0},"SubRows":null},"http://support.mozilla.org/bs":{"Attributes":null,"measures":{"Visits":3263.0,"Hits":4781.0},"SubRows":null},"http://support.mozilla.org/mk":{"Attributes":null,"measures":{"Visits":2790.0,"Hits":4339.0},"SubRows":null},"http://support.mozilla.org/sr-LATN":{"Attributes":null,"measures":{"Visits":2070.0,"Hits":3583.0},"SubRows":null},"http://support.mozilla.org/no":{"Attributes":null,"measures":{"Visits":1954.0,"Hits":3429.0},"SubRows":null},"http://support.mozilla.org/hi-IN":{"Attributes":null,"measures":{"Visits":1913.0,"Hits":3701.0},"SubRows":null},"http://support.mozilla.org/is":{"Attributes":null,"measures":{"Visits":1552.0,"Hits":2537.0},"SubRows":null},"http://support.mozilla.org/sq":{"Attributes":null,"measures":{"Visits":1548.0,"Hits":2988.0},"SubRows":null},"http://support.mozilla.com/en-US":{"Attributes":null,"measures":{"Visits":1451.0,"Hits":3358.0},"SubRows":null},"http://support.mozilla.org/eu":{"Attributes":null,"measures":{"Visits":1433.0,"Hits":2907.0},"SubRows":null},"http://support.mozilla.org/bn-BD":{"Attributes":null,"measures":{"Visits":1271.0,"Hits":2049.0},"SubRows":null},"http://support.mozilla.org/ta-LK":{"Attributes":null,"measures":{"Visits":1128.0,"Hits":1800.0},"SubRows":null},"http://support.mozilla.org/bn-IN":{"Attributes":null,"measures":{"Visits":1005.0,"Hits":2275.0},"SubRows":null},"http://support.mozilla.org/mai":{"Attributes":null,"measures":{"Visits":958.0,"Hits":1356.0},"SubRows":null},"http://support.mozilla.org/as":{"Attributes":null,"measures":{"Visits":942.0,"Hits":1438.0},"SubRows":null},"http://support.mozilla.org/ast":{"Attributes":null,"measures":{"Visits":930.0,"Hits":1352.0},"SubRows":null},"http://support.mozilla.org/hy-AM":{"Attributes":null,"measures":{"Visits":929.0,"Hits":1322.0},"SubRows":null},"http://support.mozilla.org/gl":{"Attributes":null,"measures":{"Visits":871.0,"Hits":1392.0},"SubRows":null},"http://support.mozilla.org/fur":{"Attributes":null,"measures":{"Visits":864.0,"Hits":1458.0},"SubRows":null},"http://support.mozilla.org/ga-IE":{"Attributes":null,"measures":{"Visits":856.0,"Hits":1233.0},"SubRows":null},"http://support.mozilla.org/eo":{"Attributes":null,"measures":{"Visits":844.0,"Hits":1286.0},"SubRows":null},"http://support.mozilla.org/1":{"Attributes":null,"measures":{"Visits":841.0,"Hits":1051.0},"SubRows":null},"http://support.mozilla.org/my":{"Attributes":null,"measures":{"Visits":788.0,"Hits":1166.0},"SubRows":null},"http://support.mozilla.org/mn":{"Attributes":null,"measures":{"Visits":771.0,"Hits":1227.0},"SubRows":null},"http://support.mozilla.org/ak":{"Attributes":null,"measures":{"Visits":762.0,"Hits":1274.0},"SubRows":null},"http://support.mozilla.org/fy-NL":{"Attributes":null,"measures":{"Visits":700.0,"Hits":953.0},"SubRows":null},"http://support.mozilla.org/ms":{"Attributes":null,"measures":{"Visits":675.0,"Hits":1056.0},"SubRows":null},"http://support.mozilla.org/ach":{"Attributes":null,"measures":{"Visits":631.0,"Hits":977.0},"SubRows":null},"http://support.mozilla.org/mr":{"Attributes":null,"measures":{"Visits":613.0,"Hits":1033.0},"SubRows":null},"http://support.mozilla.org/rm":{"Attributes":null,"measures":{"Visits":589.0,"Hits":807.0},"SubRows":null},"http://support.mozilla.org/si":{"Attributes":null,"measures":{"Visits":567.0,"Hits":871.0},"SubRows":null},"http://support.mozilla.org/pa-IN":{"Attributes":null,"measures":{"Visits":545.0,"Hits":759.0},"SubRows":null},"http://support.mozilla.org/ilo":{"Attributes":null,"measures":{"Visits":530.0,"Hits":757.0},"SubRows":null},"http://support.mozilla.org/te":{"Attributes":null,"measures":{"Visits":516.0,"Hits":896.0},"SubRows":null},"http://support.mozilla.org/kk":{"Attributes":null,"measures":{"Visits":490.0,"Hits":746.0},"SubRows":null},"http://support.mozilla.org/gu-IN":{"Attributes":null,"measures":{"Visits":481.0,"Hits":711.0},"SubRows":null},"http://support.mozilla.org/kn":{"Attributes":null,"measures":{"Visits":457.0,"Hits":639.0},"SubRows":null},"http://support.mozilla.org/gd":{"Attributes":null,"measures":{"Visits":376.0,"Hits":525.0},"SubRows":null},"http://support.mozilla.org/rw":{"Attributes":null,"measures":{"Visits":368.0,"Hits":553.0},"SubRows":null},"http://support.mozilla.org/ff":{"Attributes":null,"measures":{"Visits":351.0,"Hits":1259.0},"SubRows":null},"http://support.mozilla.com/de":{"Attributes":null,"measures":{"Visits":257.0,"Hits":442.0},"SubRows":null},"http://support.mozilla.org/ml":{"Attributes":null,"measures":{"Visits":254.0,"Hits":447.0},"SubRows":null},"http://support.mozilla.com/es":{"Attributes":null,"measures":{"Visits":245.0,"Hits":551.0},"SubRows":null},"http://support.mozilla.com/ja":{"Attributes":null,"measures":{"Visits":190.0,"Hits":221.0},"SubRows":null},"http://support.mozilla.org/km":{"Attributes":null,"measures":{"Visits":153.0,"Hits":213.0},"SubRows":null},"http://support.mozilla.com/fr":{"Attributes":null,"measures":{"Visits":152.0,"Hits":192.0},"SubRows":null},"http://support.mozilla.com/ru":{"Attributes":null,"measures":{"Visits":134.0,"Hits":389.0},"SubRows":null},"http://support.mozilla.org/":{"Attributes":null,"measures":{"Visits":124.0,"Hits":143.0},"SubRows":null},"http://support.mozilla.com/pt-BR":{"Attributes":null,"measures":{"Visits":75.0,"Hits":247.0},"SubRows":null},"http://support.mozilla.com/ar":{"Attributes":null,"measures":{"Visits":56.0,"Hits":71.0},"SubRows":null},"http://support.mozilla.com/it":{"Attributes":null,"measures":{"Visits":54.0,"Hits":101.0},"SubRows":null},"http://support.mozilla.com/cs":{"Attributes":null,"measures":{"Visits":42.0,"Hits":130.0},"SubRows":null},"http://support.mozilla.com/nl":{"Attributes":null,"measures":{"Visits":42.0,"Hits":58.0},"SubRows":null},"http://support.mozilla.com/pl":{"Attributes":null,"measures":{"Visits":39.0,"Hits":44.0},"SubRows":null},"http://support.mozilla.com/th":{"Attributes":null,"measures":{"Visits":27.0,"Hits":129.0},"SubRows":null},"http://support.mozilla.com/zh-TW":{"Attributes":null,"measures":{"Visits":24.0,"Hits":40.0},"SubRows":null},"http://support.mozilla.com/vi":{"Attributes":null,"measures":{"Visits":24.0,"Hits":49.0},"SubRows":null},"http://support.mozilla.com/tr":{"Attributes":null,"measures":{"Visits":18.0,"Hits":65.0},"SubRows":null},"http://support.mozilla.com/1":{"Attributes":null,"measures":{"Visits":15.0,"Hits":27.0},"SubRows":null},"http://support.mozilla.com/sv":{"Attributes":null,"measures":{"Visits":14.0,"Hits":20.0},"SubRows":null},"http://support.mozilla.com/zh-CN":{"Attributes":null,"measures":{"Visits":13.0,"Hits":13.0},"SubRows":null},"http://support.mozilla.com/ko":{"Attributes":null,"measures":{"Visits":12.0,"Hits":12.0},"SubRows":null},"http://support.mozilla.com/el":{"Attributes":null,"measures":{"Visits":9.0,"Hits":22.0},"SubRows":null},"http://support.mozilla.org/admin":{"Attributes":null,"measures":{"Visits":8.0,"Hits":11.0},"SubRows":null},"http://support.mozilla.com/hr":{"Attributes":null,"measures":{"Visits":8.0,"Hits":11.0},"SubRows":null},"http://support.mozilla.com/sl":{"Attributes":null,"measures":{"Visits":7.0,"Hits":20.0},"SubRows":null},"http://support.mozilla.org/kb":{"Attributes":null,"measures":{"Visits":7.0,"Hits":7.0},"SubRows":null},"http://support.mozilla.com/da":{"Attributes":null,"measures":{"Visits":6.0,"Hits":6.0},"SubRows":null},"http://support.mozilla.com/":{"Attributes":null,"measures":{"Visits":6.0,"Hits":7.0},"SubRows":null},"http://support.mozilla.com/et":{"Attributes":null,"measures":{"Visits":6.0,"Hits":11.0},"SubRows":null},"http://support.mozilla.com/fi":{"Attributes":null,"measures":{"Visits":6.0,"Hits":6.0},"SubRows":null},"http://support.mozilla.com/id":{"Attributes":null,"measures":{"Visits":6.0,"Hits":6.0},"SubRows":null},"http://support.mozilla.com/nb-NO":{"Attributes":null,"measures":{"Visits":5.0,"Hits":9.0},"SubRows":null},"http://support.mozilla.com/bg":{"Attributes":null,"measures":{"Visits":4.0,"Hits":6.0},"SubRows":null},"http://support.mozilla.com/pt-PT":{"Attributes":null,"measures":{"Visits":4.0,"Hits":4.0},"SubRows":null},"http://support.mozilla.com/ro":{"Attributes":null,"measures":{"Visits":3.0,"Hits":3.0},"SubRows":null},"http://support.mozilla.org/questions":{"Attributes":null,"measures":{"Visits":3.0,"Hits":4.0},"SubRows":null},"http://support.mozilla.com/hu":{"Attributes":null,"measures":{"Visits":3.0,"Hits":3.0},"SubRows":null},"http://support.mozilla.com/sr-CYRL":{"Attributes":null,"measures":{"Visits":3.0,"Hits":3.0},"SubRows":null},"http://support.mozilla.com/no":{"Attributes":null,"measures":{"Visits":3.0,"Hits":3.0},"SubRows":null},"http://support.mozilla.com/sk":{"Attributes":null,"measures":{"Visits":2.0,"Hits":2.0},"SubRows":null},"http://support.mozilla.org/services":{"Attributes":null,"measures":{"Visits":2.0,"Hits":2.0},"SubRows":null},"http://support.mozilla.com/rm":{"Attributes":null,"measures":{"Visits":2.0,"Hits":2.0},"SubRows":null},"http://support.mozilla.com/fa":{"Attributes":null,"measures":{"Visits":2.0,"Hits":2.0},"SubRows":null},"http://support.mozilla.com/he":{"Attributes":null,"measures":{"Visits":1.0,"Hits":2.0},"SubRows":null},"http://support.mozilla.com/eu":{"Attributes":null,"measures":{"Visits":1.0,"Hits":1.0},"SubRows":null},"http://support.mozilla.com/eo":{"Attributes":null,"measures":{"Visits":1.0,"Hits":1.0},"SubRows":null}}}}}'


class WebtrendsTests(TestCase):
    """Tests for the Webtrends API helper."""

    @patch.object(Webtrends, 'key_metrics')
    def test_visits(self, key_metrics):
        """Test Webtrends.visits()."""
        key_metrics.return_value = KEY_METRICS_JSON_RESPONSE

        visits = Webtrends.visits(date(2012, 01, 01), date(2012, 01, 07))

        eq_(7, len(visits))
        eq_(495974, visits['2012-01-01'])
        eq_(529301, visits['2012-01-07'])

    @patch.object(Webtrends, 'request')
    def test_visits_by_locale(self, request):
    	"""Test Webtrends.visits_by_locale()."""
    	request.return_value = L10N_METRICS_JSON_RESPONSE

    	visits = Webtrends.visits_by_locale(date(2012, 02, 11), date(2012, 03, 11))

    	eq_(77, len(visits))
    	eq_(7561779.0, visits['en-US'])
    	eq_(815609.0, visits['es'])
