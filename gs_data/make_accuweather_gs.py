import json

html_text = """<html lang="it" class="accuweather"><head>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	
	<meta charset="utf-8">
	<link rel="preload" href="/fonts/Solis-Regular.woff2" as="font" type="font/woff2" crossorigin="">

<link rel="preconnect" href="https://www.awxcdn.com">
<link rel="preconnect" href="https://securepubads.g.doubleclick.net">

<link rel="dns-prefetch" href="https://www.awxcdn.com">
<link rel="dns-prefetch" href="https://securepubads.g.doubleclick.net">
<link rel="dns-prefetch" href="https://pubads.g.doubleclick.net">

	<link rel="canonical" href="https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490">
	<title>Roma, Lazio, Italia Previsioni meteo tre giorni | AccuWeather</title>
	<meta name="Description" content="Roma, Lazio, Italia Weather Forecast, with current conditions, wind, air quality, and what to expect for the next 3 days.">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="referrer" content="origin">
	
	

	<meta property="fb:profile_id" content="AccuWeather">
<meta property="fb:app_id" content="132437483467956">
<meta property="fb:pages" content="71781612888">
<meta property="og:type" content="website">
<meta property="og:title" content="Roma, Lazio, Italia Previsioni meteo tre giorni | AccuWeather">
<meta property="og:description" content="Roma, Lazio, Italia Weather Forecast, with current conditions, wind, air quality, and what to expect for the next 3 days.">
<meta property="site_name" content="AccuWeather">
<meta property="og:url" content="https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490">
<meta property="og:image" content="https://www.accuweather.com/images/logos/aw-logo-og-meta.png">
<meta property="og:image:url" content="https://www.accuweather.com/images/logos/aw-logo-og-meta.png">
<meta property="og:image:secure_url" content="https://www.accuweather.com/images/logos/aw-logo-og-meta.png">
<meta name="twitter:site" content="https://twitter.com/accuweather">
<meta name="twitter:card" content="summary">
<meta name="twitter:text:title" content="Roma, Lazio, Italia Previsioni meteo tre giorni | AccuWeather">
<meta name="twitter:title" content="Roma, Lazio, Italia Previsioni meteo tre giorni | AccuWeather">
<meta name="twitter:description" content="Roma, Lazio, Italia Weather Forecast, with current conditions, wind, air quality, and what to expect for the next 3 days.">
<meta name="twitter:site:id" content="https://twitter.com/accuweather">
<meta name="twitter:creator" content="https://twitter.com/accuweather">
<meta name="twitter:creator:id" content="https://twitter.com/accuweather">
<meta name="twitter:image" content="https://www.accuweather.com/images/logos/aw-logo-og-meta.png">
<meta name="twitter:app:name:iphone" content="AccuWeather: Weather Tracker">
<meta name="twitter:app:id:iphone" content="U7D6TVQ9TT.com.yourcompany.TestWithCustomTabs">
<meta name="twitter:app:url:iphone" content="https://apps.apple.com/US/app/id300048137?mt=8">
<meta name="twitter:app:name:ipad" content="AccuWeather: Weather Tracker">
<meta name="twitter:app:id:ipad" content="U7D6TVQ9TT.com.yourcompany.TestWithCustomTabs">
<meta name="twitter:app:url:ipad" content="https://apps.apple.com/US/app/id300048137?mt=8">
<meta name="twitter:app:name:googleplay" content="AccuWeather Winter weather alerts &amp; forecast radar">
<meta name="twitter:app:id:googleplay" content="com.accuweather.android">
<meta name="twitter:app:url:googleplay" content="https://play.google.com/store/apps/details?id=com.accuweather.android">

	<script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202604140101/show_ads_impl_fy2021.js"></script><script src="https://securepubads.g.doubleclick.net/pagead/managed/js/gpt/m202604140101/pubads_impl_page_level_ads.js?cb=31097937"></script><script type="application/ld+json">
{
	"@context": "https://schema.org",
	"@type": "Organization",
	"name": "AccuWeather",
	"url": "https://www.accuweather.com",
	"sameAs": [
		"https://www.facebook.com/AccuWeather",
		"https://twitter.com/BreakingWeather",
		"https://www.instagram.com/accuweather",
		"https://www.youtube.com/user/accuweather"
  ]
}
</script>

		<script type="application/ld+json">
	{
		"@context": "https://schema.org",
		"@type": "Place",
		"address": {
			"@type": "PostalAddress",
			"addressLocality": "Roma, Italia",
			"addressRegion": "Lazio",
			"postalCode": ""
		},
		"geo": {
			"@type": "GeoCoordinates",
			"latitude": "41.901",
			"longitude": "12.48",
			"addressCountry": "IT",
			"postalCode": ""
		},
		"name": "Roma, Lazio, Italia"
	}
	</script>

	<script type="application/ld+json">
{
	"@context": "https://schema.org",
	"@type": "WebSite",
	"mainEntityOfPage": {
		"@type": "WebPage",
		"@id": "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490",
		"relatedLink": "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490"
	},
	"image": {
		"@type": "ImageObject",
		"url": "https://www.accuweather.com/images/logos/accuweather-dark.png",
		"height": 172,
		"width": 1200
	},
	"author": {
		"@type": "Person",
		"name": "AccuWeather"
	},
	"publisher": {
		"@context": "https://schema.org",
		"@type": "Organization",
		"name": "AccuWeather",
		"url": "https://www.accuweather.com/",
		"logo": {
			"@type": "ImageObject",
			"url": "https://www.accuweather.com/images/logos/accuweather-dark-small.png",
			"width": 163,
			"height": 23
		}
	},
	"url": "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490",
	"headline": "Roma, Lazio, Italia Previsioni meteo tre giorni",
	"description": "Roma, Lazio, Italia Weather Forecast, with current conditions, wind, air quality, and what to expect for the next 3 days."
}
</script>


		<script>window.tagEngineDataLayer = {} ?? {};</script>
	<script>
		window.tagEngineDataLayer = window.tagEngineDataLayer || {};
		Object.assign(window.tagEngineDataLayer, {
			adDataAdc: {
				adInfo: {"fdate":"20260420","lang":"it","ut":"1","advelvet":"5","inview":"ititrome213490weather-forecast213490:wbr,wb","bot":"0","pgview":"1","partner":"google_search_accuweather","ufdb":"LII7","city":"Rome","country":"IT","state":"62","dma":null,"key":"213490","region":"eur","lat":"41.901","lon":"12.48","browser":"safari","connection":"mobile_vhigh_5000","wx_seg":"101100100,102102102,109101100,108102100,100108101,102100100,102101100,102103100,107100102,100111100,107101102,108103101,101103100,100113103,108104101,101105100,110100100,109104100,109105100,100106102,110101101,109100102,108101102,103100102,109103102,103101102,101106102,108100102,100109105,102104102,104100103,101104101,104101101,100109102,109102102,100114105,109106102,101107101,101108101,101102102,105100102,107103102,100114102,100114101,101101101","alertscategory":"SEVERE,SEVERE","alertssource":"it,it","alertstypeid":"IT312,IT312","cuhd":"64","cuhi":"67","cuuv":"6","cuwd":"8","cuwx":"3","realfeel":"75,a80,b75,c75,d75","cuaq":"3","fc1hi":"74","fc1lo":"54","fc1wx":"2","lfscategory":"rain","lfsday":"3","lfsseverity":"5","lfs":"5_rain_3","pt":"0","userid":"active","userid3p":"missing","sub":"free","auth":"false","site":"adc"},
				adSlots: {"top":{"bidders":[{"bidder":"google","params":{"sizes":"970x250,728x90,fluid,970x90","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":640474,"position":"atf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"triplelift","params":{"inventoryCode":"accuweather_d_top_leaderboard_pbjs","floor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"criteo","params":{"networkId":12212,"pubid":"3852","uid":"472391","bidFloor":0.02,"bidFloorCur":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"pubmatic","params":{"publisherId":"34576","adSlot":"Web_Top","lat":"41.9","lon":"12.48","kadfloor":"0.02","currency":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"ix","params":{"siteId":"197759","bidFloor":0.02,"bidFloorCur":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"openx","params":{"delDomain":"accuweather-d.openx.net","unit":"539580665","customParams":{"fdate":["20260420"],"advelvet":["5"],"pgview":["1"],"partner":["google_search_accuweather"],"ufdb":["LII7"],"country":["IT"],"state":["62"],"wx_seg":["101100100","102102102","109101100","108102100","100108101","102100100","102101100","102103100","107100102","100111100","107101102","108103101","101103100","100113103","108104101","101105100","110100100","109104100","109105100","100106102","110101101","109100102","108101102","103100102","109103102","103101102","101106102","108100102","100109105","102104102","104100103","101104101","104101101","100109102","109102102","100114105","109106102","101107101","101108101","101102102","105100102","107103102","100114102","100114101","101101101"],"alertscategory":["SEVERE","SEVERE"],"alertssource":["it","it"],"alertstypeid":["IT312","IT312"],"cuhd":["64"],"cuhi":["67"],"cuuv":["6"],"cuwd":["8"],"cuwx":["3"],"realfeel":["75","a80","b75","c75","d75"],"fc1hi":["74"],"fc1lo":["54"],"fc1wx":["2"],"lfscategory":["rain"],"lfsday":["3"],"lfsseverity":["5"],"lfs":["5_rain_3"],"pt":["0"],"adunit":["/6581/web/it/top/weather/local_home"]},"customFloor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"ttd","params":{"supplySourceId":"accuweather","publisherId":"1","bidfloor":0.02,"currency":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"google","params":{"sizes":"970x250,728x90,fluid,970x90","Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":1518598,"position":"atf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.8,"Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"triplelift","params":{"inventoryCode":"Acccuweather_Prebid_web_top_BIN","floor":1.0,"Is_Buy_It_Now":true},"isBuyItNow":true}],"slot":"top","adDivId":"top","adUnitCode":"/6581/web/it/top/weather/local_home","upr":0.2,"tid":"9dd0b2b1-7eb7-4a6d-9e23-ea1517f11f30"},"oop":{"bidders":[{"bidder":"google","params":{"sizes":"oop","Is_Buy_It_Now":false},"isBuyItNow":false}],"slot":"oop","adDivId":"oop","adUnitCode":"/6581/web/it/oop/weather/local_home","upr":0.02,"tid":"a26adecb-8076-4249-bf62-1a48c2837603"},"interstitial":{"bidders":[{"bidder":"google","params":{"sizes":"interstitial","Is_Buy_It_Now":false},"isBuyItNow":false}],"slot":"interstitial","adDivId":"interstitial","adUnitCode":"/6581/web/it/interstitial/weather/local_home","upr":4.0,"tid":"0500a863-2742-4a3e-b37b-2f316e76abf5"},"top_right":{"bidders":[{"bidder":"google","params":{"sizes":"300x250,300x600,160x600,120x600,fluid","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":2745920,"position":"atf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"triplelift","params":{"inventoryCode":"accuweather_d_topright_rectangle_pbjs","floor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"criteo","params":{"networkId":12212,"pubid":"3852","uid":"472390","bidFloor":0.02,"bidFloorCur":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"pubmatic","params":{"publisherId":"34576","adSlot":"Web_TopRight","lat":"41.9","lon":"12.48","kadfloor":"0.02","currency":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"ix","params":{"siteId":"197760","bidFloor":0.02,"bidFloorCur":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"openx","params":{"delDomain":"accuweather-d.openx.net","unit":"539580668","customParams":{"fdate":["20260420"],"advelvet":["5"],"pgview":["1"],"partner":["google_search_accuweather"],"ufdb":["LII7"],"country":["IT"],"state":["62"],"wx_seg":["101100100","102102102","109101100","108102100","100108101","102100100","102101100","102103100","107100102","100111100","107101102","108103101","101103100","100113103","108104101","101105100","110100100","109104100","109105100","100106102","110101101","109100102","108101102","103100102","109103102","103101102","101106102","108100102","100109105","102104102","104100103","101104101","104101101","100109102","109102102","100114105","109106102","101107101","101108101","101102102","105100102","107103102","100114102","100114101","101101101"],"alertscategory":["SEVERE","SEVERE"],"alertssource":["it","it"],"alertstypeid":["IT312","IT312"],"cuhd":["64"],"cuhi":["67"],"cuuv":["6"],"cuwd":["8"],"cuwx":["3"],"realfeel":["75","a80","b75","c75","d75"],"fc1hi":["74"],"fc1lo":["54"],"fc1wx":["2"],"lfscategory":["rain"],"lfsday":["3"],"lfsseverity":["5"],"lfs":["5_rain_3"],"pt":["0"],"adunit":["/6581/web/it/top_right/weather/local_home"]},"customFloor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"ttd","params":{"supplySourceId":"accuweather","publisherId":"1","bidfloor":0.02,"currency":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"google","params":{"sizes":"300x250,300x600,160x600,120x600,fluid","Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":2745916,"position":"atf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.8,"Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"triplelift","params":{"inventoryCode":"Acccuweather_Prebid_web_topright_BIN","floor":1.0,"Is_Buy_It_Now":true},"isBuyItNow":true}],"slot":"top_right","adDivId":"top_right","adUnitCode":"/6581/web/it/top_right/weather/local_home","upr":0.1,"tid":"353585cb-966e-4178-935b-e73d00963095"},"bottom_right":{"bidders":[{"bidder":"google","params":{"sizes":"300x250,300x600,160x600,120x600,300x251,300x601,fluid","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":2745918,"position":"btf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"pubmatic","params":{"publisherId":"34576","adSlot":"Web_BottomRight","lat":"41.9","lon":"12.48","kadfloor":"0.02","currency":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"ix","params":{"siteId":"197765","bidFloor":0.02,"bidFloorCur":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"openx","params":{"delDomain":"accuweather-d.openx.net","unit":"539580673","customParams":{"fdate":["20260420"],"advelvet":["5"],"pgview":["1"],"partner":["google_search_accuweather"],"ufdb":["LII7"],"country":["IT"],"state":["62"],"wx_seg":["101100100","102102102","109101100","108102100","100108101","102100100","102101100","102103100","107100102","100111100","107101102","108103101","101103100","100113103","108104101","101105100","110100100","109104100","109105100","100106102","110101101","109100102","108101102","103100102","109103102","103101102","101106102","108100102","100109105","102104102","104100103","101104101","104101101","100109102","109102102","100114105","109106102","101107101","101108101","101102102","105100102","107103102","100114102","100114101","101101101"],"alertscategory":["SEVERE","SEVERE"],"alertssource":["it","it"],"alertstypeid":["IT312","IT312"],"cuhd":["64"],"cuhi":["67"],"cuuv":["6"],"cuwd":["8"],"cuwx":["3"],"realfeel":["75","a80","b75","c75","d75"],"fc1hi":["74"],"fc1lo":["54"],"fc1wx":["2"],"lfscategory":["rain"],"lfsday":["3"],"lfsseverity":["5"],"lfs":["5_rain_3"],"pt":["0"],"adunit":["/6581/web/it/bottom_right/weather/local_home"]},"customFloor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"google","params":{"sizes":"300x250,300x600,160x600,120x600,300x251,300x601,fluid","Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":2745914,"position":"btf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.4,"Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"triplelift","params":{"inventoryCode":"Acccuweather_Prebid_Web_bottomright_BIN","floor":0.45,"Is_Buy_It_Now":true},"isBuyItNow":true}],"slot":"bottom_right","adDivId":"bottom_right","adUnitCode":"/6581/web/it/bottom_right/weather/local_home","upr":0.1,"tid":"4fdfdea3-bd87-4cf0-9290-91d52861cb9e"},"bottom":{"bidders":[{"bidder":"google","params":{"sizes":"970x250,728x90,728x91,970x251,fluid","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":640476,"position":"btf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"pubmatic","params":{"publisherId":"34576","adSlot":"Web_Bottom","lat":"41.9","lon":"12.48","kadfloor":"0.02","currency":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"ix","params":{"siteId":"197764","bidFloor":0.02,"bidFloorCur":"USD","Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"openx","params":{"delDomain":"accuweather-d.openx.net","unit":"539580672","customParams":{"fdate":["20260420"],"advelvet":["5"],"pgview":["1"],"partner":["google_search_accuweather"],"ufdb":["LII7"],"country":["IT"],"state":["62"],"wx_seg":["101100100","102102102","109101100","108102100","100108101","102100100","102101100","102103100","107100102","100111100","107101102","108103101","101103100","100113103","108104101","101105100","110100100","109104100","109105100","100106102","110101101","109100102","108101102","103100102","109103102","103101102","101106102","108100102","100109105","102104102","104100103","101104101","104101101","100109102","109102102","100114105","109106102","101107101","101108101","101102102","105100102","107103102","100114102","100114101","101101101"],"alertscategory":["SEVERE","SEVERE"],"alertssource":["it","it"],"alertstypeid":["IT312","IT312"],"cuhd":["64"],"cuhi":["67"],"cuuv":["6"],"cuwd":["8"],"cuwx":["3"],"realfeel":["75","a80","b75","c75","d75"],"fc1hi":["74"],"fc1lo":["54"],"fc1wx":["2"],"lfscategory":["rain"],"lfsday":["3"],"lfsseverity":["5"],"lfs":["5_rain_3"],"pt":["0"],"adunit":["/6581/web/it/bottom/weather/local_home"]},"customFloor":0.02,"Is_Buy_It_Now":false},"isBuyItNow":false},{"bidder":"google","params":{"sizes":"970x250,728x90,728x91,970x251,fluid","Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"rubicon","params":{"accountId":12562,"siteId":135890,"zoneId":2745912,"position":"btf","userId":"7d695715xd89fx4158xab9bx5114c8ba51db","floor":0.2,"Is_Buy_It_Now":true},"isBuyItNow":true},{"bidder":"triplelift","params":{"inventoryCode":"Acccuweather_Prebid_Web_bottom_BIN","floor":0.2,"Is_Buy_It_Now":true},"isBuyItNow":true}],"slot":"bottom","adDivId":"bottom","adUnitCode":"/6581/web/it/bottom/weather/local_home","upr":0.1,"tid":"6bd57a3e-858b-44b1-9189-780249e58f13"}},
				globalAdConfig: {"prebidTimeout":1000,"awxTimeout":1000,"gptEnableSingleRequest":false,"gptLazyLoading":"{fetchMarginPercent:150,renderMarginPercent:75,mobileScaling:1.0}","skipGoogleAdManager":true,"prebidBundleId":"a","testVariant":"","disableInitialAdLoad":true,"javascriptHead":"","javascriptBody":""},
				ortbConfig: {"name":"AccuWeather","domain":"accuweather.com","categories":["IAB7","IAB10","IAB15","IAB20","223","274","390","464","653"],"sectionCategories":[""],"pageCategories":["IAB15-10","IAB20-14","IAB20-19","390","659"],"keywords":"","pageUrl":"","referrerUrl":"","isOptimizedForMobile":true,"hasPrivacyPolicy":true,"publisher":{"name":"AccuWeather","domain":"accuweather.com","categories":["IAB7","IAB10","IAB15","IAB20","223","274","390","464","653"]},"content":{"title":"","url":"","categories":["IAB15-10","IAB20-14","IAB20-19","390","659"],"productQuality":"1","context":"5","keywords":"","sourceRelationship":1,"language":"","data":{"name":"accuweather.com","extensions":{"segtax":"4"},"segments":[{"name":"id","value":"390"},{"name":"id","value":"659"}]}}},
				platform: 'web',
				ppid: '7d695715xd89fx4158xab9bx5114c8ba51db',
				userData: {"city":"SIZIANO","continent":2,"countryCode":"IT","county":"","lat":45.33,"long":9.2,"regionCode":"25","throughput":"vhigh","bw":"5000","networkType":"mobile","network":"fastweb","zipCodes":[{"primary":""}],"device":{"browserVersion":"26"}},
			}
		});
	</script>

	<style>
		@font-face {
			font-family: 'Solis';
			src: url('/fonts/Solis-Regular.woff2') format('woff2');
			font-weight: 400;
			font-style: normal;
			font-display: swap;
		}
	</style>
	<style>
		:root {
			--bg: #1f1f1f;
			--header-bg: #1f1f1f;
			--header-bg-top: #1f1f1f;
		}
	</style>

	

	
<script>
	window.pushlyTranslations = {"en":{"phrase":"Get AccuWeather alerts as they happen with our browser notifications.","enableNotifications":"Enable Notifications","noThanks":"No, Thanks","enabled":"Notifications Enabled","thanks":"Thanks! We'll keep you informed."},"es":{"phrase":"Recibe alertas de AccuWeather en su navegador en el momento","enableNotifications":"Habilitar Notificaciones","noThanks":"No, Gracias","enabled":"Notificaciones Habilitadas","thanks":"¡Gracias! Te mantendremos al tanto."}};
</script>


	<script>
	var gaAppConfig = {
  "snowfallMap": true,
  "mapCta": true,
  "iceChart": true,
  "winterOutlookCard": true,
  "winterUpcomingCard": true,
  "impactedCities": true,
  "tempWindChart": true,
  "snowfallChart": true,
  "postEventCta": true,
  "winterCenterMap": true
};
	var userCookie = {"cDate":"2026-04-16","isDarkMapStyle":false,"lang":"it","rl":["213490"],"tp":"C","clk":"undefined","ccb":true,"userContentAffinity":{}};
	var recentLocations = [{"adminArea":{"englishName":"Lazio","id":"62","localizedName":"Lazio"},"alertCount":0,"country":{"englishName":"Italy","id":"IT","localizedName":"Italia"},"icon":3,"key":"213490","localizedName":"Roma","postalCode":"","temp":"21°","realFeel":"24°","isDayTime":true}];
	var currentLocation = {"plumeLabsLink":"https://air.plumelabs.com/air-quality-in-rome-diq2","englishName":"Rome","gmtOffset":2.0,"hasAlerts":true,"hasForecastConfidence":true,"hasPollen":true,"hasMinuteCast":true,"hasFutureRadar":true,"lat":41.901,"lon":12.48,"region":{"englishName":"Europe","id":"EUR","localizedName":"Europa"},"timeZone":"CEST","timeZoneCode":"CEST","administrativeArea":{"englishName":"Lazio","id":"62","localizedName":"Lazio"},"country":{"englishName":"Italy","id":"IT","localizedName":"Italia"},"key":"213490","localizedName":"Roma","primaryPostalCode":"","source":"AccuWeather"};
	var weatherEvents = [];
	var userData = {"city":"SIZIANO","continent":2,"countryCode":"IT","county":"","lat":45.33,"long":9.2,"regionCode":"25","throughput":"vhigh","bw":"5000","networkType":"mobile","network":"fastweb","zipCodes":[{"primary":""}],"device":{"browserVersion":"26"}};
	var maplibre = { style: 'https://accutilerprod.z14.web.core.windows.net/Styles/accu-light-row.json' };
	var dts = { token: 'de13920f574d420984d3080b1fa6132b' };
	setTimeout(function () {
		var reg = new RegExp('(\\s|^)' + 'ads-not-loaded' + '(\\s|$)');
		if (document.body.hasAttribute('class')) {
			document.body.setAttribute('class', document.body.getAttribute('class').replace(reg, ' '));
		}
	}, 3000);
</script>

	



	


<script>
	window.tagEngineDataLayer = window.tagEngineDataLayer || {};

	Object.assign(window.tagEngineDataLayer, {
		isSPA: false,
		pageGroup: "three-day",
		raine: {
			raineV1Host: "https://raine.accuweather.com",
			raineV2Host: "https://raine.accuweather.com",
			enabledVersions: [2],
			raineV1: {
				pageView: null,
			},
			raineV2: {
				pageView: {"testGroup":"raine_variant","platformVersion":"2.3.27.0","pageInfo":{"group":"three-day","url":"/it/it/rome/213490/weather-forecast/213490","referrer":"https://www.google.com/"},"adInfo":{"code":"/6581/web/it/top/weather/local_home","status":"active","cookie3p":"missing"},"sessionInfo":{"id":"188d0cdb-a7df-4d85-941a-15103d83d347","partner":"google_search_accuweather","utm":{}},"userInfo":{"userPartner":"","id":"aabb62c2-3a89-44c2-86c5-ead1b04c96df","language":"it","country":"IT","region":"25","city":"SIZIANO","start":"2026-04-16"},"isBot":false,"infra":"glacier","id":"b810153a-9116-4917-a563-bb9cac2d596b","platform":"web","weather":{"key":"213490"},"device":{"name":"safari","brand":"Apple","version":"26","category":"desktop"},"time":"2026-04-20T09:57:55Z"},
			},
		}
	});
</script>


	<script>
    if (window.tagEngineDataLayer?.ketch?.isEnabled !== false) {
      // https://cdn.ketchjs.com/plugins/v1/tcf/stub.js
      window.__gpp_addFrame=function(e){if(!window.frames[e])if(document.body){var t=document.createElement("iframe");t.style.cssText="display:none",t.name=e,document.body.appendChild(t)}else window.setTimeout(window.__gpp_addFrame,10,e)},window.__gpp_stub=function(){var e=arguments;if(__gpp.queue=__gpp.queue||[],__gpp.events=__gpp.events||[],!e.length||1==e.length&&"queue"==e[0])return __gpp.queue;if(1==e.length&&"events"==e[0])return __gpp.events;var t=e[0],p=e.length>1?e[1]:null,n=e.length>2?e[2]:null;const a=localStorage.getItem("_ketch_gpp_v1_");let s=null;if(a&&(s=JSON.parse(window.atob(a))),"ping"===t)p(s||{gppVersion:"1.1",cmpStatus:"stub",cmpDisplayStatus:"hidden",signalStatus:"not ready",sectionList:[],applicableSections:[],gppString:"",parsedSections:{}},!0);else if("addEventListener"===t){"lastId"in __gpp||(__gpp.lastId=0),__gpp.lastId++;var i=__gpp.lastId;__gpp.events.push({id:i,callback:p,parameter:n}),p({eventName:"listenerRegistered",listenerId:i,data:!0,pingData:s||{gppVersion:"1.1",cmpStatus:"stub",cmpDisplayStatus:"hidden",signalStatus:"not ready",sectionList:[],applicableSections:[],gppString:"",parsedSections:{}}},!0)}else if("removeEventListener"===t){for(var _=!1,l=0;l<__gpp.events.length;l++)if(__gpp.events[l].id==n){__gpp.events.splice(l,1),_=!0;break}p({eventName:"listenerRemoved",listenerId:n,data:_,pingData:s||{gppVersion:"1.1",cmpStatus:"stub",cmpDisplayStatus:"hidden",signalStatus:"not ready",sectionList:[],applicableSections:[],gppString:"",parsedSections:{}}},!0)}else"hasSection"===t?p(!1,!0):"getSection"===t||"getField"===t?p(null,!0):__gpp.queue.push([].slice.apply(e))},window.__gpp_msghandler=function(e){var t="string"==typeof e.data;try{var p=t?JSON.parse(e.data):e.data}catch(e){p=null}if("object"==typeof p&&null!==p&&"__gppCall"in p){var n=p.__gppCall;window.__gpp(n.command,(function(p,a){var s={__gppReturn:{returnValue:p,success:a,callId:n.callId}};e&&e.source&&e.source.postMessage&&e.source.postMessage(t?JSON.stringify(s):s,"*")}),"parameter"in n?n.parameter:null,"version"in n?n.version:"1.1")}},"__gpp"in window&&"function"==typeof window.__gpp||(window.__gpp=window.__gpp_stub,window.addEventListener("message",window.__gpp_msghandler,!1),window.__gpp_addFrame("__gppLocator"));

      // https://cdn.ketchjs.com/plugins/v1/gpp/stub.js
      !function(){const e=()=>{const e="__tcfapiLocator",t=[],n=window;let o,s,a=n;for(;a;){try{if(a.frames[e]){o=a;break}}catch(e){}if(a===n.top)break;a=a.parent}o||(!function t(){const o=n.document,s=!!n.frames[e];if(!s)if(o.body){const t=o.createElement("iframe");t.style.cssText="display:none",t.name=e,o.body.appendChild(t)}else setTimeout(t,5);return!s}(),n.__tcfapi=function(...e){if(!e.length)return t;if("setGdprApplies"===e[0])e.length>3&&2===parseInt(e[1],10)&&"boolean"==typeof e[3]&&(s=e[3],"function"==typeof e[2]&&e[2]("set",!0));else if("ping"===e[0]){const t=localStorage.getItem("_ketch_tcf_ping_v1_");t?"function"==typeof e[2]&&e[2](JSON.parse(window.atob(t))):"function"==typeof e[2]&&e[2]({gdprApplies:s,cmpLoaded:!1,cmpStatus:"stub"})}else if("addEventListener"===e[0]){const n=localStorage.getItem("_ketch_tcf_tcdata_v1_");n?"function"==typeof e[2]&&e[2](JSON.parse(window.atob(n)),!0):t.push(e)}else t.push(e)},n.addEventListener("message",(function(e){const t="string"==typeof e.data;let n={};if(t)try{n=JSON.parse(e.data)}catch(e){}else n=e.data;const o="object"==typeof n&&null!==n?n.__tcfapiCall:null;o&&window.__tcfapi(o.command,o.version,(function(n,s){let a={__tcfapiReturn:{returnValue:n,success:s,callId:o.callId}};e&&e.source&&e.source.postMessage&&e.source.postMessage(t?JSON.stringify(a):a,"*")}),o.parameter)}),!1))};"undefined"!=typeof module?module.exports=e:e()}();

      // ketch boot script
      (function () {
        window.semaphore = window.semaphore || [];
        window.ketch = function () {
          window.semaphore.push(arguments);
        };
        var e = document.createElement("script");
        e.type = "text/javascript";
        e.src = "https://global.ketchcdn.com/web/v3/config/accuweather/website_smart_tag/boot.js";
        e.defer = e.async = !0;
        document.getElementsByTagName("head")[0].appendChild(e);
      })();
    }
</script><script type="text/javascript" src="https://global.ketchcdn.com/web/v3/config/accuweather/website_smart_tag/boot.js" async="" defer=""></script>
<link rel="stylesheet" href="https://www.accuweather.com/tags/common/ketch/ketch-2d5abe96.css">

	
	<script type="module" async="" src="https://www.accuweather.com/tags/shared/prebid/prebid-a-7411b6f1.js"></script>


	<script>(async () => {function l(i){return`[${i}]
`}function I(i,e){if(!i&&(!e||Array.isArray(e)&&e.length===0))return;const t=[];return i&&t.push(i),e&&(Array.isArray(e)?t.push(...e):t.push(e)),t}class S{timeouts=new Map;setTimeout(e,t,a){this.clearTimeout(e);const n=setTimeout(()=>{t(),this.clearTimeout(e)},a);this.timeouts.set(e,n)}clearTimeout(e){const t=this.timeouts.get(e);t&&(clearTimeout(t),this.timeouts.delete(e))}}const R=window.awxTimeoutProcessor??new S;window.awxTimeoutProcessor=R;function M(i){if(i<=5e3){if(i%500===0)return 500;if(i%1e3===0)return 1e3}return Math.floor(i/2)}function k(i,e,{callerScope:t,logger:a}={}){const n=Date.now();return new Promise(s=>{let r=e();const g=()=>{const E=Date.now()-n,D=[t??"","isReadyPromise"].filter(Boolean).join("::");return window.debugDataLayer?.enabled&&(a?a("debug",{scope:D,message:`Ready in ${E}ms`}):console.debug(l("isReadyPromise"),`Ready in ${E}ms`)),s(r)};if(r)return g();window.awxLogger?.withScope(`${t}::isReadyPromise`).debug("Waiting for isReadyChecker to return true");let d,c;const m=()=>{clearInterval(c),clearTimeout(d),d=void 0,c=void 0};c=setInterval(()=>{if(r=e(),r)return m(),g()},M(i)),d=setTimeout(()=>(m(),g()),i)})}const T={type:"application/json"},P=5e3,C={pageLeave:6e5,timers:3e4},$={timers:"timers",pageView:"pageview",pageLeave:"pageleave",genericEvents:"events",updateProfile:"update-profile"},N={1:["pageView","pageLeave"],2:["pageView","pageLeave","updateProfile","genericEvents"]},O={ads:"adInfo",bot:"isBot",page:"pageInfo",user:"userInfo",test:"testGroup",session:"sessionInfo",version:"platformVersion"},p=()=>!!window.adInfo?.userid3p&&!!window.adInfo?.userid;function j(i){return!!i?.pageView?.ads?.code&&p()}function z(i){return!!i?.pageView?.adInfo?.code&&p()}function u(i){return Array.isArray(window.tagEngineDataLayer?.raine?.enabledVersions)?i===void 0?window.tagEngineDataLayer.raine.enabledVersions.length>0:window.tagEngineDataLayer.raine.enabledVersions.includes(i):!1}function f(i,e){return e??=w()?.[i],u(i)&&!!e}function G(i,e){e??=w()?.[i];const t=()=>i===1?j(e):z(e);return u(i)&&f(i,e)&&t()}function y(i,e){return e?Object[i===1?"keys":"values"](O).every(n=>n in e):!1}function V(i,e=!0){return e?G(i):f(i)}async function B(i,e=5e3){return k(e,()=>V(i),{callerScope:"isRaineReadyAsync"})}const h={isReady:V,isEnabled:u,isAvailable:f,isDataValid:y,isReadyAsync:B};function w(){return{1:window.tagEngineDataLayer?.raine?.raineV1,2:window.tagEngineDataLayer?.raine?.raineV2}}function b(){return{eventsState:w(),eventsMap:N}}function H(){const i=window.tagEngineDataLayer?.pageGroup;if(typeof i=="string"&&i.trim()!==""&&i.toLowerCase()!=="app")return i.trim().toLowerCase();const e=window.location.pathname.split("/").filter(a=>a.length>0);if(e.length===0)return"home";if(e[0].toLowerCase()==="app")return e[1]?e[1].toLowerCase()==="account"&&e[2]?e[2].toLowerCase():e[1].toLowerCase():"home";const t=e.findIndex((a,n)=>/^(\d+)$/.test(a)&&n<e.length-1);return t!==-1&&e[t+1]?e[t+1].toLowerCase():e[0].toLowerCase()}class U{pageIndex=0;version;events;isAdsSetupComplete=p();isInitialized=!1;maxInitializeDelay=P;debug=!1;isSPA=!1;timeoutDurations;logger=void 0;constructor(e,t){this.version=e,this.events=t??["pageview","pageleave"],this.isSPA=!!window.tagEngineDataLayer.isSPA;const a=window.tagEngineDataLayer.raine;this.debug=!!window.debugDataLayer?.enabled,this.maxInitializeDelay=a?.initializeDelay||P,this.timeoutDurations={...C,...a?.timeoutDurations}}isReady(){return this.isInitialized}getLogger(e){return this.logger??=window.awxLogger?.withScope("Analytics"),e?this.logger?.withScope(e):this.logger}setIsAdsSetupComplete(e){this.log("debug",{scope:"setIsAdsSetupComplete",message:`RaineV${this.version} ads setup complete...`,args:{instance:this}}),this.isAdsSetupComplete=e}setIsInitialized(e){this.log("debug",{scope:"setIsInitialized",message:`RaineV${this.version} is initialized...`,args:{instance:this}}),this.isInitialized=e}getRaineHost(){const e=`raineV${this.version}Host`;let t;if(window.tagEngineDataLayer.raine&&e in window.tagEngineDataLayer.raine&&window.tagEngineDataLayer.raine[e]&&(t=window.tagEngineDataLayer.raine[e]),!t){this.log("error",{scope:"getRaineHost",message:`RaineV${this.version} host not found in data layer`});return}return t}sendAnalyticsEventData(e,t,a,n=!1){const s={hostUrl:e,event:t,data:a};this.log("debug",{scope:`sendAnalyticsEventData::${t}`,message:"Sending analytics event data.",args:s}),n||window.debugDataLayer?.analytics?.raine?.requestService==="fetch"?fetch(e,{method:"POST",keepalive:!0,priority:"high",body:JSON.stringify(a),headers:{"Content-Type":"application/json","X-Raine-Version":this.version.toString()}}).then(r=>{r.ok?this.log("debug",{scope:`sendAnalyticsEventData::${t}`,message:"Successfully sent analytics event data.",args:{...s,response:{...r,text:r.text()||"",json:r.json()||{}}}}):this.log("error",{scope:`sendAnalyticsEventData::${t}`,message:"Failed to send analytics event data.",args:this.debug?s:void 0})}).catch(r=>{this.log("error",{scope:`sendAnalyticsEventData::${t}`,message:"Error occurred while sending analytics event data.",args:this.debug?{...s,error:r}:void 0})}):navigator?.sendBeacon(e,new Blob([JSON.stringify(a)],T))?this.log("debug",{scope:`sendAnalyticsEventData::${t}`,message:"Successfully queued analytics event data using sendBeacon.",args:s}):this.log("error",{scope:`sendAnalyticsEventData::${t}`,message:"Failed to queue analytics event data using sendBeacon.",args:this.debug?s:void 0})}sendRaineEvent(e,t,a=!1){const n=this.getRaineHost();if(this.isInitialized&&n&&t){const s=`${n}/tracker/v${this.version}/${e}`;this.sendAnalyticsEventData(s,e,t,a)}else{this.log("warning",{scope:"sendRaineEvent",message:`No data provided for RAINE event ${e}`,args:this.debug?{raineHost:n,data:t}:void 0});return}}}class x extends U{raineVersionedData;pageLeaveFired=!1;pageView;pageViewEvent=()=>new CustomEvent("updatePageViewOnPageChanged",{detail:this.pageView});pageLeave;constructor(e,t,a){super(e,t),e&&(this.version=e),this.pageView=a,this.raineVersionedData=w(),this.pageLeave=this.createPageLeaveEvent(),this.resetPageLeaveEventTimeout()}clearTimeout(e){window.awxTimeoutProcessor.clearTimeout(e)}resetEventTimeout(e,t){const a=e==="pageleave"?6e5:3e4;window.awxTimeoutProcessor.setTimeout(e,t.bind(this),this.timeoutDurations[e]??a)}resetPageLeaveEventTimeout(){this.resetEventTimeout("pageleave",this.sendPageLeaveEvent.bind(this,!0))}setPageGroup(e){e??=window.tagEngineDataLayer.pageGroup;let t=H();if(t=t?.toLowerCase()||e||"home",window.tagEngineDataLayer.raine=window.tagEngineDataLayer.raine||{},this.version===1)this.pageView.page.group=t;else if(this.version===2){const a=this.pageView;a.pageInfo.group=t,window.tagEngineDataLayer.raine={...window.tagEngineDataLayer.raine,raineV2:{...window.tagEngineDataLayer.raine.raineV2,pageView:a}}}}initRaine(){if(window.tagEngineDataLayer.raine){if(this.isInitialized){this.log("warning",{scope:"initRaine",message:"Raine object already initialized."});return}}else{this.log("error",{scope:"initRaine",message:"RAINE object not found in data layer."});return}this.setIsInitialized(!0),this.updatePageView(),this.sendPageViewEvent()}getUserOffset(){const e=r=>("0"+r).slice(-2),t=new Date().getTimezoneOffset(),a=Math.floor(Math.abs(t)/60),n=Math.abs(t)%60;return`${t>0?"-":"+"}${e(a)}:${e(n)}`}onPageChange(){this.logEvent("onPageChange"),this.sendPageLeaveEvent(),window.awxPerformance.startNewPageSession(++this.pageIndex),window.awxEventListenerProcessor.resetScrollDepth(),this.resetTimersOnPageChange(),window.dispatchEvent(this.pageViewEvent()),this.updatePageView(),this.sendPageViewEvent(),this.pageLeaveFired=!1,this.pageLeave=this.createPageLeaveEvent()}logEvent(e){this.log("debug",{scope:e,message:`Handling event logic for ${e}`})}onAdsReload(){this.logEvent("onAdsReload"),this.setIsAdsSetupComplete(!1)}onSetupAdInfo(){this.logEvent("onSetupAdInfo"),this.setIsAdsSetupComplete(!0),this.setPageViewAdInfo()}onVisibilityChange(){document.visibilityState==="hidden"&&!this.pageLeaveFired&&this.sendPageLeaveEvent()}initEventProcessor(){window.addEventListener("beforeunload",this.sendPageLeaveEvent.bind(this,!0)),document.addEventListener("visibilitychange",this.onVisibilityChange.bind(this)),this.isSPA&&window.addEventListener("popstate",this.onPageChange.bind(this)),window.addEventListener("onSetupAdInfo",this.onSetupAdInfo.bind(this)),window.addEventListener("adsReload",this.onAdsReload.bind(this)),this.initRaine()}initEventListeners(){this.log("debug",{scope:"initEventListeners",message:"Initializing event listeners."}),this.initEventProcessor()}log=(e,{message:t,args:a,scope:n})=>{if(!t&&!a)return;const s=[`RAINE${this.version?`v${this.version}`:""}`,n??""].filter(Boolean),r=s.join("::"),g=this.getLogger(r);if(g&&e in g){g[e](t,a);return}const d=I(t,a);if(e==="debug"&&!this.debug||!d||d.length===0)return;const c=console[e==="warning"?"warn":e];c(`[Analytics::${s.join("::")}]
`,...d)};updateRaineConstants(e){if(!window.tagEngineDataLayer.raine){this.log("error",{scope:"updateRaineConstants",message:"RAINE object not found in data layer."});return}window.tagEngineDataLayer.raine?.constants||(window.tagEngineDataLayer.raine.constants=b()),window.tagEngineDataLayer.raine.constants={...window.tagEngineDataLayer.raine.constants,eventsState:{...window.tagEngineDataLayer.raine.constants.eventsState,[this.version]:{...window.tagEngineDataLayer.raine.constants.eventsState[this.version],...e}}}}}class F extends x{constructor(){super(1,["pageview","pageleave"],window.tagEngineDataLayer.raine.raineV1.pageView),this.initEventListeners()}getPageGroup(){return this.setPageGroup(),window.tagEngineDataLayer.raine?.raineV1?.pageView?.page.group||"home"}setPageViewAdInfo(){const e="adInfo"in window?window.adInfo:{},t=this.pageView??{};t.ads.status="userid"in e?e.userid:"",t.ads.cookie3p="userid3p"in e?e.userid3p:"",window.tagEngineDataLayer.raine.raineV1.pageView=t}refreshRaineData(){if(window.tagEngineDataLayer.raine)return this.pageLeave=this.createPageLeaveEvent(),this.updateRaineConstants({pageView:this.pageView,pageLeave:this.pageLeave}),window.tagEngineDataLayer.raine}updatePageView(){this.pageView=this.createPageViewEvent(window.tagEngineDataLayer.raine?.raineV1?.pageView),window.tagEngineDataLayer.raine?.raineV1&&(window.tagEngineDataLayer.raine.raineV1.pageView=this.pageView)}createPageViewEvent(e){const t=e??this.pageView??{};return this.setPageViewAdInfo(),{...t,page:{...t.page,group:this.getPageGroup()},user:{...t.user,offset:this.getUserOffset()}}}sendPageViewEvent(){window.tagEngineDataLayer.raine?.raineV1Host?(this.sendAnalyticsEventData(`${window.tagEngineDataLayer.raine.raineV1Host}/rainev1/p`,"pageview",this.pageView),this.log("debug",{scope:"sendPageViewEvent",message:"Event pageview successfully sent.",args:{pageView:this.pageView,raineV1Events:window.tagEngineDataLayer.raine.raineV1}})):this.log("warning",{scope:"sendPageViewEvent",message:"Event pageview is undefined."})}createPageLeaveEvent(){const e=[],t=this.pageView?.id??window.tagEngineDataLayer.raine?.raineV1?.pageView?.id??"";return window.awxPerformance.iterateAwxPerformanceMarks(window.awxPerformance.getAwxPerformanceMarksByPageSession(this.pageIndex),(a,n)=>{this.pageIndex===a.detail.pageIndex&&e.push(n)}),e.push({name:"raine:timeOnPage",time:window.awxPerformance.getTimeOnPage(this.pageIndex)}),this.pageLeave={id:t,scroll:window.awxEventListenerProcessor.getScrollDepth(),timers:e},this.updateRaineConstants({pageLeave:this.pageLeave}),this.pageLeave}resetTimersOnPageChange(){this.resetPageLeaveEventTimeout()}sendPageLeaveEvent(e=!1){(e||this.isSPA||document.visibilityState==="hidden")&&!this.pageLeaveFired&&window.tagEngineDataLayer.raine?.raineV1Host&&(this.pageView&&this.createPageLeaveEvent()?(this.sendAnalyticsEventData(`${window.tagEngineDataLayer.raine.raineV1Host}/rainev1/leavepage`,"pageleave",this.pageLeave),this.pageLeaveFired=!0,this.log("debug",{scope:"sendPageLeaveEvent",message:"Event pageleave successfully sent.",args:{pageLeave:this.pageLeave}})):this.log("warning",{scope:"sendPageLeaveEvent",message:"Unable to sent pageleave event. Check the args to ensure they are valid.",args:{force:e,isSPA:this.isSPA,documentVisibilityState:document.visibilityState,isPageLeaveSent:this.pageLeaveFired,pageView:this.pageView,pageLeave:this.pageLeave}}))}}class q extends x{updateProfile;genericEvents={id:"",time:"",events:[]};timersEvent;constructor(){super(2,Object.values($).map(e=>e),window.tagEngineDataLayer.raine.raineV2.pageView),this.updateProfile=window.tagEngineDataLayer.raine?.raineV2?.updateProfile,this.updateProfile&&(this.updateProfile.user={...this.updateProfile.user,...this.pageView?.userInfo||{},offset:this.getUserOffset()},this.sendUpdateProfileEvent()),this.initEventListeners(),window.addEventListener("onUpdateProfile",this.onUpdateProfile.bind(this)),this.resetTimersEventTimeout(),this.initGenericEvents(),window.trackRaineEvent=this.trackRaineEvent.bind(this),window.sendGenericEvents=this.sendGenericEvents.bind(this)}resetTimersOnPageChange(){this.log("debug",{scope:"resetTimersOnPageChange",message:"Resetting timers and page leave event on page change."}),this.resetPageLeaveEventTimeout(),this.resetTimersEventTimeout()}onUpdateProfile(e){e.detail?(this.log("debug",{scope:"onUpdateProfile",message:"Update profile event received.",args:{updateProfile:e}}),this.updateProfile=e.detail,this.sendUpdateProfileEvent()):this.log("warning",{scope:"onUpdateProfile",message:"Update profile event is undefined.",args:{updateProfile:e}})}resetTimersEventTimeout(){this.resetEventTimeout("timers",this.sendTimersEvent.bind(this))}refreshRaineData(){if(window.tagEngineDataLayer.raine)return this.pageLeave=this.createPageLeaveEvent(),this.updateRaineConstants({pageView:this.pageView,pageLeave:this.pageLeave,updateProfile:this.updateProfile,genericEvents:this.genericEvents,timers:this.createTimersEvent()}),window.tagEngineDataLayer.raine}getPageGroup(){return this.setPageGroup(),window.tagEngineDataLayer.raine?.raineV2?.pageView?.pageInfo.group||"home"}setPageViewAdInfo(){(!window.adInfo?.userid3p||!window.adInfo?.userid)&&this.log("debug",{scope:"setPageViewAdInfo",message:"Ad info is not available.",args:{adInfo:window.adInfo}}),window.tagEngineDataLayer.raine||this.log("debug",{scope:"setPageViewAdInfo",message:"RAINE data layer is not available."}),this.pageView={...this.pageView,adInfo:{...this.pageView?.adInfo,status:window.adInfo?.userid||"",cookie3p:window.adInfo?.userid3p||""}},window.tagEngineDataLayer.raine.raineV2.pageView=this.pageView}updatePageView(){this.pageView=this.createPageViewEvent(window.tagEngineDataLayer.raine?.raineV2?.pageView),this.initGenericEvents(),window.tagEngineDataLayer.raine?.raineV2&&(window.tagEngineDataLayer.raine.raineV2.pageView=this.pageView)}createPageViewEvent(e){this.pageView=e??this.pageView??{};const t=this.getPageGroup(),a=this.getUserOffset();return this.log("debug",{scope:"createPageViewEvent",message:"Creating pageView data for sending to processor.",args:{pageView:this.pageView,adInfo:window.adInfo,pageGroup:t,userOffset:a}}),this.setPageViewAdInfo(),this.pageView={...this.pageView,pageInfo:{...this.pageView.pageInfo,group:t},userInfo:{...this.pageView.userInfo,offset:a}},this.log("debug",{scope:"createPageViewEvent",message:"RAINE data added for pageView.",args:{pageView:this.pageView}}),this.pageView}createPageLeaveEvent(){const e=this.pageView??{id:"",time:""};return this.pageLeave={id:e.id,time:e.time,adblock:!window.supportsAds,scroll:window.awxEventListenerProcessor.getScrollDepth(),duration:window.awxPerformance.getTimeOnPage(this.pageIndex)},this.pageLeave}sendPageLeaveEvent(e=!1){const t=e||this.isSPA||document.visibilityState==="hidden",a=()=>this.debug?{force:e,isSPA:this.isSPA,documentVisibilityState:document.visibilityState,isPageLeaveSent:this.pageLeaveFired,pageView:this.pageView,pageLeave:this.pageLeave}:void 0;if(this.pageLeaveFired){this.log("debug",{scope:"sendPageLeaveEvent",message:"Page leave event has already been sent for this page session. Skipping..."});return}const n=this.getRaineHost();if(!n||!t||!this.pageView){this.log("warning",{scope:"sendPageLeaveEvent",message:"Unable to sent pageleave event. Check the args to ensure they are valid.",args:a()});return}this.clearTimeout("pageleave");const s=this.createPageLeaveEvent();this.updateRaineConstants({pageLeave:s});const r=`${n}/tracker/v${this.version}/pageleave`;this.sendAnalyticsEventData(r,"pageleave",s),this.pageLeaveFired=!0,this.sendTimersEvent(),this.sendGenericEvents()}sendPageViewEvent(){document.visibilityState!=="hidden"&&this.sendRaineEvent("pageview",this.pageView)}sendUpdateProfileEvent(){this.sendRaineEvent("update-profile",this.updateProfile)}createTimersEvent(){const e={time:this.pageView.time,platform:this.pageView.platform,infra:this.pageView.infra,country:this.pageView.userInfo.country,timers:[]};return window.awxPerformance.iterateAwxPerformanceMarks(window.awxPerformance.getAwxPerformanceMarksByPageSession(this.pageIndex,"cache"),(t,a)=>{const n={...a,tags:[]};this.pageIndex===t.detail.pageIndex&&e.timers.push(n)}),this.updateRaineConstants({timers:e}),e}initGenericEvents(){this.genericEvents={id:this.pageView?.id??"",time:this.pageView?.time??"",events:[]}}sendGenericEvents(e=!1){this.genericEvents.events.length>0&&(this.sendRaineEvent("events",this.genericEvents,e),this.genericEvents.events=[])}trackRaineEvent(e,t,a,n){this.genericEvents.events.push({category:e,action:t,label:a,value:n}),25<=this.genericEvents.events.length&&this.sendGenericEvents()}sendTimersEvent(){if(this.clearTimeout("timers"),this.timersEvent=this.createTimersEvent(),this.timersEvent.timers.length===0){this.log("debug",{scope:"sendTimersEvent",message:"No timers found to send.",args:{timersEvent:this.timersEvent}});return}this.sendRaineEvent("timers",this.timersEvent),window.awxPerformance.clearAwxPerformanceMarks("cache")}}class A{debug;constructor(e){this.debug=e?.debug??!!window.debugDataLayer?.enabled}}class v extends A{eventsListMap={};events=[];constructor(e,t){super(t);let a={};Array.isArray(e)&&e.length>0&&typeof e[0]=="string"?e.forEach(n=>{a[n]=[]}):typeof e=="object"&&(a=e),this.setEventsListMap(a),this.registerScopedEvents()}setEventsListMap(e){this.eventsListMap=e,this.events=Object.keys(this.eventsListMap)}addCallbacksToEventListener(e,t){const a=this.eventsListMap[e];a&&a.length>0&&a.forEach(n=>{n(t)})}}class K extends v{registerScopedEvents(){window.pbjs=window.pbjs||{},pbjs.que=pbjs.que||[],pbjs.que&&pbjs.que.push(()=>{this.events.forEach(e=>{pbjs.onEvent(e,()=>{window.awxPerformance.createPerformanceMark(`prebid:${e}`)})})})}}class W extends v{allowedAdSlotIds=["top"];truncateAdId(e){if(e){const t=e.split("/");if(t.length>1){const a=t.findIndex(n=>n==="6581");e=t[a+3]}}return e}isAdSlotIdTrackable(e){return this.allowedAdSlotIds.some(t=>e.includes(t))}registerScopedEvents(){window.googletag=window.googletag||{cmd:[]},googletag.cmd&&googletag.cmd.push(()=>{this.events.forEach(e=>{googletag.pubads().addEventListener(e,t=>{const a=this.truncateAdId(t.slot.getSlotElementId());this.isAdSlotIdTrackable(a)&&window.awxPerformance.createPerformanceMark(`gpt:${e}:${a}`)})})})}}const J=["DOMContentLoaded","windowLoad"],X=[];class _ extends v{registerScopedEvents(){this.events.forEach(e=>{const t=X.includes(e);window.addEventListener(e,a=>{this.addCallbacksToEventListener(e,a);const n=e==="load"?"windowLoad":e;J.includes(n)&&window.awxPerformance.createPerformanceMark(`document:${n}`)},{passive:t})})}}class Q extends A{eventListeners=new Map;scrollDepth=0;callCount=0;maxCallCount=0;constructor(e){super(e),this.initListeners(),window.tagEngineDataLayer.raine?.enabledVersions&&(this.maxCallCount=window.tagEngineDataLayer.raine.enabledVersions.length)}getScrollDepth(){return this.scrollDepth}resetScrollDepth(){if(this.callCount+1<this.maxCallCount){this.callCount++;return}this.callCount=0,this.scrollDepth=0}getEventListeners(){return Array.from(this.eventListeners.values())}setScrollDepth(e){const{scrollTop:t,scrollHeight:a,clientHeight:n}=document.documentElement,s=a-n,r=Math.round(t/s*100);r>this.scrollDepth&&(this.scrollDepth=Math.min(100,Math.max(0,r)))}initListeners(){const e=["auctionInit","auctionEnd","requestBids","setTargeting"];this.eventListeners.has("prebid")||this.eventListeners.set("prebid",new K(e));const t=["slotRequested","slotOnload","slotRenderEnded"];this.eventListeners.has("googleTag")||this.eventListeners.set("googleTag",new W(t)),this.eventListeners.has("domLoaded")||this.eventListeners.set("domLoaded",new _({DOMContentLoaded:[],load:[],scroll:[this.setScrollDepth.bind(this)]}))}}function Y(i){return new Promise(e=>{let a=0;const n=()=>{window.ketch||a>=i?e(window.ketch):(a+=100,setTimeout(n,100))};n()})}function Z(i,e){const t=w();if(!t||!t?.[i])return;const a=t[i];if(!e||e==="settings")return a;if(a&&y(i,a)&&e in a)return a[e]}function ee(){window.tagEngineDataLayer.raine={...window.tagEngineDataLayer.raine,constants:b(),utils:{isRaine:h,getEventOrEventPropData:Z}}}class te{pageIndex=0;callCount=0;maxCallCount=0;awxPerformanceMarks=new Map;sentMarksCache=new Map;getPageIndex(){return this.pageIndex}getPageSessionPerformanceMark(e=this.pageIndex){const t=this.getPerformanceEntry(`awx:${e}:start`,"mark");if(t)return t}startNewPageSession(e,t="cache"){this.callCount++<this.maxCallCount||this.pageIndex===e||(this.pageIndex=e,this.clearAwxPerformanceMarks(t),this.createPerformanceMark("start",{prefix:"awx"}),this.callCount=0)}calculatePageSessionRelativeDuration(e,t){t??=e.detail?.pageIndex??this.pageIndex;const a=this.getPageSessionPerformanceMark(t);return Math.round(e.startTime-(a?.startTime??0))}getTimeOnPage(e){e??=this.pageIndex;const t=this.getPageSessionPerformanceMark(e);return Math.round(performance.now()-(t?.startTime??0))}createPerformanceMark(e,t={prefix:"aw",pageIndex:this.pageIndex}){t.prefix??="aw",t.pageIndex??=this.pageIndex;const a=this.getAwxPerformanceMarkName(e,t.prefix);if(this.awxPerformanceMarks.has(a))return this.awxPerformanceMarks.get(a);const n=this.getPerformanceEntry(a,"mark");if(n)return n;const s=this._createAwxPerformanceMark(a,t);return this.awxPerformanceMarks.set(a,s),s}getAwxPerformanceMarksByPageSession(e,t="marks"){const a=[];return this.iterateAwxPerformanceMarks(window.performance.getEntriesByType("mark"),n=>{if(n.detail.pageIndex===e){if(t==="cache"){if(this.sentMarksCache.has(n.name))return;this.sentMarksCache.set(n.name,n)}a.push(n)}}),a}clearAwxPerformanceMarks(e="cache"){["both","marks"].includes(e)&&this.iterateAwxPerformanceMarks(window.performance.getEntriesByType("mark"),t=>{performance.clearMarks(t.name)}),["both","cache"].includes(e)&&this.awxPerformanceMarks.clear()}performanceMarkToTimerItem(e){return{name:e.detail.name,time:this.calculatePageSessionRelativeDuration(e)}}getAwxPerformanceMarkName(e,t="aw"){const a=t||"aw";return e.startsWith(`${a}:`)?e:`${a}:${this.pageIndex}:${e}`}createPerformanceMeasurement(e){const t=this.getAwxPerformanceMarkName(e),a=`${t}:measure`,n=this.getPerformanceEntry(a,"measure");if(n instanceof PerformanceMeasure)return n;const s=this.getPageSessionPerformanceMark();return!s&&this.pageIndex>0&&window.awxLogger?.withScope("AwxPerformanceApi::createPerformanceMeasurement").error(`No page session mark found for page index ${this.pageIndex}.`),window.performance.measure(a,s?.name??{},t)}getPerformanceEntry(e,t){const a=window.performance.getEntriesByName(e,t);if(a.length>0)return a[a.length-1]}getAwxPerformanceMark(e,t="aw"){const a=this.getAwxPerformanceMarkName(e,t);return this.awxPerformanceMarks.has(a)?this.awxPerformanceMarks.get(a):this.getPerformanceEntry(a,"mark")}iterateAwxPerformanceMarks(e,t){e.forEach(a=>{a instanceof PerformanceMark&&this.isAwxPerformanceMark(a)&&t(a,this.performanceMarkToTimerItem(a))})}isAwxPerformanceMark(e){return(a=>{const n=a?.split(":");return n?.[0]==="aw"&&n?.length>2})(e.name)}_createAwxPerformanceMark(e,t={prefix:"aw",pageIndex:this.pageIndex}){const a=this.getAwxPerformanceMarkName(e,t.prefix),n=new RegExp(`^${t.prefix}:(\\d+):`);return window.performance.mark(a,{detail:{name:e.replace(n,""),pageIndex:t.pageIndex}})}getAwxPerformanceMarks(e="cache"){if(e==="cache")return Array.from(this.awxPerformanceMarks.values());const t=[];return this.iterateAwxPerformanceMarks(window.performance.getEntriesByType("mark"),a=>{t.push(a)}),t}}const ae=window.awxEventListenerProcessor??new Q;window.awxEventListenerProcessor=ae;const ie=window.awxPerformance??new te;window.awxPerformance=ie;ee();const o={};function L(){const i=l("tagEngine::enableRaineAnalytics");try{!o?.[1]&&h.isEnabled(1)&&(o[1]=new F),!o?.[2]&&h.isEnabled(2)&&(o[2]=new q)}catch(e){window.awxLogger?window.awxLogger.withScope("tagEngine::enableRaineAnalytics").debug("Error initializing RAINE",e):window.debugDataLayer?.enabled&&console.debug(`${i}Error initializing RAINE`,e)}window.debugDataLayer?.enabled&&(o?.[1]||o?.[2])&&(window.debugDataLayer.analytics={...window.debugDataLayer.analytics,raine:{...window.debugDataLayer.analytics?.raine||{requestService:"beacon"},instances:o}},window.awxLogger?window.awxLogger.withScope("tagEngine::enableRaineAnalytics").debug("RAINE instances initialized",o):window.debugDataLayer?.enabled&&console.debug(`${i}RAINE instances initialized`,o))}Y(1500).then(i=>{if(i)i("on","consent",function(e){window.debugDataLayer={...window.debugDataLayer,ketch:{consent:e}},e.purposes?.analytics&&L()});else{if(window.awxLogger)window.awxLogger.withScope("tagEngine::waitForKetch").debug("Ketch unavailable... Enabling RAINE analytics.");else if(window.debugDataLayer?.enabled){const e=l("tagEngine::waitForKetch");console.debug(`${e}Ketch unavailable... Enabling RAINE analytics.`)}L()}});
//# sourceMappingURL=raine.inline-191939e4.js.map
})();</script><script>(async () => {function v(e){try{const t=document.getElementById(`client-data-store-${e}`);if(t&&t.innerText){const o=JSON.parse(t.innerText);return window.awxLogger?.withScope(`tagEngine::parseClientDataStore::${e}`).debug("Successfully parsed store data",o),o}}catch(t){window.awxLogger?.withScope(`tagEngine::parseClientDataStore::${e}`).error(`Could not parse client data store '${e}'`,t)}window.awxLogger?.withScope(`tagEngine::parseClientDataStore::${e}`).debug(`${e}: Could not parse JSON data, likely missing client-data-store element.`)}function E(e,t=!1){try{return JSON.parse(e)}catch(o){if(t)throw o;return window.awxLogger?.withScope("tagEngine::tryParseJSON").error("Could not parse JSON data.",{jsonString:e,error:o}),null}}const W=()=>new Promise(e=>{typeof window.__gpp=="function"&&window.__gpp("ping",t=>{t?.gppString&&e()}),typeof window.ketch=="function"?window.ketch("on","consent",()=>{e()}):e()}),M=e=>{const{adData:t={},adDataAdc:o}=window.tagEngineDataLayer;if(o)return o;const i=window.location.pathname.replace("/app","").replaceAll("/","");return t[e||i||"home"]||{...t.home,adSlots:{}}},J=({globalAdConfig:e,ppid:t,ortbConfig:o,isPrebidDisabled:i,userData:a,platform:d,hashedEmail:l})=>{const r={prebidTimeout:750,awxTimeout:1e4,disableInitialAdLoad:!0,gptEnableSingleRequest:!0,gptLazyLoading:"{}",buyItNowSkipGoogleAdManager:!0,isPrebidDisabled:i,userData:a,...e};t&&(r.ppid=t),o&&(r.ortbConfig=o),d&&(r.platform=d),l&&(r.hashedEmail=l,window.eh2=l);try{const s=E(r.gptLazyLoading.replace(/(['"])?([a-z0-9A-Z_]+)(['"])?:/g,'"$2": '),!0);typeof s=="object"&&Object.keys(s).length>0?r.gptLazyLoading=s:delete r.gptLazyLoading}catch(s){window.awxLogger?.withScope("Ads::setupGlobalAdConfig").debug("Error parsing gptLazyLoading",s),delete r.gptLazyLoading}window.globalAdConfig=r},Q=e=>{const t=new Set(["advelvet","alertscategory","alertssource","alertstypeid","country","cuhd","cuhi","cuuv","cuwd","cuwx","dma","fdate","hour","lfs","lfscategory","lfsday","lfsseverity","partner","pgview","pt","realfeel","site","state","wx_seg","ufdb"]);return Object.entries(e).reduce((o,[i,a])=>(t.has(i)&&(o[i]=a?.split(",")),o),{})},$=({adSlots:e})=>{const t=new Map;if(e&&Object.values(e).length){const i=Object.values(e)[0].adUnitCode.split("/")[2]!=="web"?["adhesion","top","middle","native","infeed","bottom","oop"]:["top","top_right","infeed","bottom_right","middle","native","bottom","oop"];window.adInfo.sub!=="premium-plus"&&i.push("interstitial");const a=Q(window.adInfo);Object.values(e).sort((d,l)=>i.indexOf(d.slot)-i.indexOf(l.slot)).filter(d=>{const l=i.indexOf(d.slot)>-1,r=d.bidders?.some(s=>s.bidder==="google");return l&&r}).forEach(d=>{d.winner={auction:0},d.sizes=d.bidders.find(l=>l.bidder==="google")?.params?.sizes.split(",").map(l=>l.includes("x")?l.split("x").map(Number):l),d.bidders.forEach(l=>{for(const[r,s]of Object.entries(l.params))s==="%%targeting%%"?l.params[r]={adunit:[d.adUnitCode],...a}:typeof s=="string"&&s.includes("%%")&&delete l.params[r]}),t.set(d.adDivId,d)})}window.adsOnPage=t},Z=()=>{const e="awx_pv",t=new Date;t.setDate(t.getDate()+1),t.setHours(0,0,0,0);let o=E(localStorage.getItem(e));o?.ttl&&new Date<o.ttl?o.val+=1:o={val:1,ttl:+t},localStorage.setItem(e,JSON.stringify(o))},D=e=>A(v("userSettings")?.isMetric?e*9/5+32:e),A=e=>e<0?-Math.round(-e):Math.round(e),Y=new CustomEvent("onSetupAdInfo");function z({adInfo:e={}}){const{ortbConfig:t,testVariant:o}=window.globalAdConfig,i=E(localStorage.getItem("awx_pv")||'{ "val": 1 }');e.pgview=i.val.toString(),e.hour=new Date().getHours().toString();const a=document.documentElement.clientWidth,d=document.documentElement.clientHeight,l=u=>Math.ceil(u/10)*10;e.viewport=`${l(a)}x${l(d)}`,e.site==="adc"?e.site=a>=768?a>=1024?"desktop":"tablet":"mobile":e.site="one",t?.pageCategories&&(e.iabctax=t.pageCategories.join(","));const r=new URLSearchParams(window.location.search);r.get("adClicks")&&(e.clicks=r.get("adClicks"));const s=window.location.pathname.split("/").filter(Boolean);if(r.get("from")&&s?.[1].toLowerCase()==="today"){e.from=r.get("from");const u=window.location.href.replace(`?from=${r.get("from")}`,"");window.history.replaceState({},document.title,u)}else e.from=null;r.get("adtestkey")?e.test=r.get("adtestkey"):o&&(e.test=o),e.userid="active";const n=v("alerts");n?.length>0&&(e.alertscategory=n.map(u=>u.category).join(","),e.alertssource=n.map(u=>u.countryCode).join(","),e.alertstypeid=n.map(u=>u.typeId).join(","));const c=v("currentConditions");c&&(e.cuhd=A(c.extended?.humidityValue).toString(),e.cuhi=A(c.apparentTempImperial).toString(),e.cuuv=A(c.extended?.uv?.value).toString(),e.cuwd=A(c.windSpeedImperial).toString(),e.cuwx=c.iconCode.toString(),e.realfeel=A(D(c.realFeelValue)).toString());const p=v("currentAirQuality");if(p){const u=p.overallPlumeLabsIndex;let h="0";u>=0&&u<20?h="1":u>=20&&u<50?h="2":u>=50&&u<100?h="3":u>=100&&u<150?h="4":u>=150&&u<250?h="5":u>=250&&(h="6"),e.cuaq=h}const g="abcd",w=v("dailyForecasts");w&&w.slice(0,4).forEach((u,h)=>{e.realfeel+=`,${g[h]}${A(D(u.day.realFeelValue))}`});const f=v("localForecastSummary");if(f){const u=f.category?f.category.replace("/","-"):"x",h=Math.abs(new Date(f.startDate)-new Date)/(1e3*60*60*24),B=Math.min(Math.round(h),10)+1;e.lfscategory=u,e.lfsseverity=f.severity.toString(),e.lfsday=B.toString(),e.lfs=`${f.severity}_${u}_${B}`}e.pt=localStorage.getItem("timeOnPage")||"0",window.adInfo=e,window.dispatchEvent(Y);const m=JSON.parse(localStorage.getItem("adResults"));i.val===1&&m&&(m.previousRatio=m.filledAds/m.possibleAds,m.filledAds=0,m.possibleAds=0),window.adResults=m||{}}function S(e,t){if(e==null)return e;const o=Math.pow(10,t);let i=Math.round(e*o)/o;const a=1/o;return i===+e&&(e>=0?i+=a:i-=a),parseFloat(i.toFixed(t))}const O=e=>Object.keys(e).map(t=>`${t}=${e[t]}`).join("&"),X=({adUnitCode:e,adObject:t,customTargeting:o={}})=>{let i=e.split("/");i[3]="bin_prebid";const a=i.join("/"),d={...o,...window.adInfo||{},...window.getUprTargeting?.(t)||{},ppid:window.globalAdConfig?.ppid},l={iu:a,sz:"1x1",c:Math.round(Date.now()/1e3),t:encodeURIComponent(O(d)),m:"text/html"},r=`https://securepubads.g.doubleclick.net/gampad/adx?${O(l)}`,s=document.createElement("iframe");s.setAttribute("src",r),s.setAttribute("style","width:0;height:0;display:none"),s.setAttribute("aria-hidden","true"),s.id=`${t.adDivId}-bin-tracker`,document.body.appendChild(s)},F=[],j=window._floorsByBidId||=new Map,ee=e=>Array.isArray(e)?e[0]?.bidFloor??e[0]?.floor??null:e?.bidFloor??e?.floor??null;window._binAliases=window._binAliases||new Set;const U={rubicon:52,triplelift:28,appnexus:32},te=e=>{const t=`${e}-bin`;if(window._binAliases.has(t))return t;try{const o=U[e]?{gvlid:U[e]}:void 0;pbjs.aliasBidder(e,t,o),window._binAliases.add(t)}catch(o){window.awxLogger?.withScope("Ads::ensureBinAlias").debug(`Failed to alias bin bidder ${e} -> ${t}`,o)}return t},oe=()=>{const{ppid:e,ortbConfig:t,userData:o,platform:i,hashedEmail:a}=window.globalAdConfig;let d={};window.adInfo.country?.toLowerCase()==="us"&&(d={country:"usa",region:window.adInfo.state,metro:window.adInfo.dma,city:window.adInfo.city,zip:window.adInfo.zip,type:3,lat:S(window.adInfo.lat,4),lon:S(window.adInfo.lon,4)});const l={data:{}};["userid","userid3p","partner","pgview","pt","viewport","hour"].forEach(g=>{window.adInfo&&window.adInfo[g]&&(l.data[g]=window.adInfo[g].replaceAll("-","neg"))});const r=`${window.location.protocol}//${window.location.host}${window.location.pathname}`,s={name:t.name||"AccuWeather",domain:t.domain||"www.accuweather.com",cat:t.categories||["IAB-7","IAB7-4","IAB15-10","IAB20","288","390","653"],page:r,ref:document.referrer,mobile:t.isOptimizedForMobile?1:0,privacypolicy:t.hasPrivacyPolicy?1:0,publisher:{name:t.publisher.name||"AccuWeather",domain:t.publisher.domain||"www.accuweather.com",cat:t.publisher.categories||["IAB-7","IAB7-4","IAB15-10","IAB20","288","390","653"]},content:{language:window.adInfo.lang?.substring(0,2),title:document.title,keywords:t.content.keywords,url:r,cat:t.content.categories,prodq:parseInt(t.content.productQuality),context:parseInt(t.content.context),sourcerelationship:typeof t.content.sourceRelationship=="number"?t.content.sourceRelationship:t.content.sourceRelationship?.toLowerCase()==="direct"?1:0,data:[{name:t.content.data.name,ext:{...t.content.data.extensions,segtax:parseInt(t.content.data.extensions.segtax)},segment:t.content.data.segments}]},sectioncat:t.sectionCategories,pagecat:t.pageCategories,keywords:t.keywords,ext:{data:{}}};if(["advelvet","country","cuhd","cuhi","cuuv","cuwd","cuwx","dma","fdate","state","wx_seg","ufdb","alertscategory","alertssource","alertstypeid","site","realfeel"].forEach(g=>{window.adInfo&&window.adInfo[g]&&(s.ext.data[g]=window.adInfo[g].replaceAll("-","neg").split(","))}),window.adsOnPage.has("top")){const{upr:g,bidders:w}=window.adsOnPage.get("top"),f=w.find(m=>m.bidder==="rubicon"&&m.isBuyItNow);s.ext.data.bin_top=f?.params?.floor,s.ext.data.upr_top=g}const n={debug:window.debugDataLayer?.prebidDebug||window.location.search.includes("pbjs_debug=true"),bidderTimeout:window.globalAdConfig?.prebidTimeout,enableSendAllBids:!1,disableAjaxTimeout:!0,maxRequestsPerOrigin:6,enableTIDs:!0,bidderSequence:"fixed",priceGranularity:{buckets:[{precision:2,max:3,increment:.01},{precision:2,max:8,increment:.05},{precision:2,max:20,increment:.5},{precision:2,max:100,increment:1}]},userSync:{filterSettings:{iframe:{bidders:"*",filter:"exclude"}},syncsPerBidder:3,aliasSyncEnabled:!0,syncDelay:3e3,userIds:[{name:"sharedId",storage:{type:"cookie",name:"_pubcid",expires:30}},{name:"criteo"},{name:"33acrossId",params:{pid:"0014000000xvF2DAAU"},storage:{name:"33acrossId",type:"html5",expires:90,refreshInSeconds:8*3600}},{name:"unifiedId",params:{partner:"vtlti0n"}}]},deviceAccess:!0,cache:{url:"https://prebid.adnxs.com/pbc/v1/cache"},rubicon:{singleRequest:!0},yahoossp:{endpoint:"https://c2shb.ssp.yahoo.com/bidRequest",singleRequestMode:!0},useBidCache:!1,bidCacheFilterFunction:g=>g.mediaType!=="video",timeoutBuffer:0,ortb2:{site:s,user:{ext:l,geo:d},device:{geo:{type:2,lat:S(o.lat,4),lon:S(o.long,4),city:o.city,country:o.countryCode,metro:String(o.dma),region:o.regionCode,zip:o.zipCodes?.[0]?.primary}}},realTimeData:{auctionDelay:100,dataProviders:[{name:"gamera",params:{},waitForIt:!0},{name:"scope3",params:{orgId:"accuweather_xz6b85se",includeKey:"axei",excludeKey:"axex",macroKey:"axem",timeout:100,debugMode:!1}}]}};window.adInfo.site==="one"&&(n.ortb2.site.ext.context={environment:"webview",site_page:r},n.ortb2.device.devicetype=1,n.ortb2.device.ua=window.navigator.userAgent);const c={name:"connectId",params:{pixelId:"58872"}};a?c.params.he=a:c.params.puid=e,n.userSync.userIds.push(c),a&&n.userSync.userIds.push({name:"uid2",params:{serverPublicKey:"UID2-X-P-MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEPKcMe5poNz1E2xltVpOwbp4txbEYCsrr8xkSEXwKamd2LoSSvBJCL4hCMv2Ad9elOUpMRnAUp7pdbzcNoP+SNQ==",subscriptionId:"xwoSMLaGio",emailHash:a}});const p={name:"pubProvidedId",params:{eids:[{source:"accuweather.com",uids:[{id:e,atype:1,ext:{stype:"ppuid"}}]}]}};if(window.localStorage?.OPTABLE_RESOLVED)try{const g=["adnxs.com","indexexchange.com","adsrvr.org","rubiconproject.com","pubmatic.com","triplelift.com"],w=E(window.localStorage.OPTABLE_RESOLVED)?.ortb2?.user?.eids;w?.length>0&&(w.forEach(f=>{g.includes(f.source)&&p.params.eids.push(f)}),window.adInfo.campaign?window.adInfo.campaign+=",optable":window.adInfo.campaign="optable")}catch(g){window.awxLogger?.withScope("Ads::prebidSetup").debug("Error parsing OPTABLE_RESOLVED",g)}if(n.userSync.userIds.push(p),n.consentManagement={gpp:{cmpApi:"iab",timeout:8e3}},de(o.countryCode)&&(n.consentManagement.gdpr={cmpApi:"iab"}),i==="ios"||i==="android"){const g=i==="ios"?"https://apps.apple.com/us/app/accuweather-weather-forecast/id300048137":"https://play.google.com/store/apps/details?id=com.accuweather.android",w=(window.adInfo?.sub??"free").trim().toLowerCase()==="free"?0:1;n.ortb2.app={name:s.name,bundle:i==="ios"?"300048137":"com.accuweather.android",domain:s.domain,storeurl:g,cat:s.cat,sectioncat:s.sectioncat,ver:window.adInfo?.appVersion,privacypolicy:s.privacypolicy,paid:w,publisher:s.publisher,content:s.content,ext:s.ext},delete n.ortb2.site}return n},ie=e=>{pbjs.setConfig(e),pbjs.bidderSettings={standard:{storageAllowed:!0}},window.globalAdConfig.hashedEmail&&pbjs.setBidderConfig({bidders:["criteo"],config:{ortb2:{user:{ext:{data:{eids:[{source:"accuweather.com",uids:[{id:window.globalAdConfig.hashedEmail,atype:3,ext:{stype:"hemsha256"}}]}]}}}}}}),pbjs.onEvent("auctionInit",t=>{t.bidderRequests.forEach(o=>{o.bids.forEach(i=>{i.isBuyItNow&&F.push(i.bidId)})})}),pbjs.onEvent("bidRequested",t=>{(t.bids||[]).forEach(o=>{let i=parseFloat(ee(o.params));Number.isFinite(i)||(i=0);const a=o.requestId||o.bidId;j.set(a,i)})}),pbjs.onEvent("bidResponse",t=>{const o=t.requestId||t.bidId,i=j.get(o);i!=null&&t.cpm<i&&(t.cpm=0,t.ad=t.nurl="",t.bidderResponseDelivered=!0,t.status="rejected")})},q={top:["300x250","320x50","300x50","336x280","728x90","970x250","970x90"],top_right:["300x250","300x600","160x600"],bottom_right:["300x250","300x600","160x600"],bottom:["300x250","320x50","300x50","300x600","336x280","728x90","970x250","970x90"],adhesion:["320x50","300x50"],middle:["300x250","320x50","300x50","300x600","336x280"],native:["1x1","2x2","300x250"],infeed:["1x1","2x2"]},k=()=>{window.adsOnPage.forEach(e=>{const{sizes:t,slot:o,adUnitCode:i,tid:a}=e;let{bidders:d}=e;if(["oop","interstitial","outstream","rewarded"].includes(o)||!d)return;d=d.filter(c=>c.bidder!=="google");const r=d.filter(c=>!c.isBuyItNow),s=d.filter(c=>c.isBuyItNow),n={banner:{sizes:t.filter(c=>{const p=q[o]||[];return Array.isArray(c)&&p.indexOf(c.join("x"))>-1})}};if((o==="native"||o==="infeed")&&(n.native={type:"image"}),window.logAdEvent(`Prebid: Add ad unit: ${i}`),pbjs.addAdUnits){const c={bids:r,mediaTypes:n,code:i,ortb2Imp:{exp:60,ext:{data:{pbadslot:i},gpid:i,tid:a}}};window.adInfo.site==="one"&&(c.ortb2Imp.ext.webview=1),pbjs.addAdUnits(c)}if(window.globalAdConfig.disableInitialAdLoad&&s.length){const c=`${i}-bin`,p=s.map(g=>{const w=te(g.bidder);return{...g,bidder:w}});if(pbjs.addAdUnits){const g={bids:p,mediaTypes:n,code:i,ortb2Imp:{exp:60,ext:{data:{pbadslot:c},gpid:c}}};window.adInfo.site==="one"&&(g.ortb2Imp.ext.webview=1),pbjs.addAdUnits(g)}}})},N=()=>{window.adsOnPage.forEach(e=>{const{sizes:t,slot:o,adUnitCode:i,bidders:a}=e;if(["oop","interstitial","outstream","rewarded"].includes(o)||!a)return;const l={banner:{sizes:t.filter(s=>{const n=q[o]||[];return Array.isArray(s)&&n.indexOf(s.join("x"))>-1})}};(o==="native"||o==="infeed")&&(l.native={type:"image"});const r=a.filter(s=>s.bidder==="ttd"&&!s.isBuyItNow).map(s=>({...s,bidder:"thetradedesk"}));if(r.length){window.logAdEvent(`Open Ads: Add ad unit: ${i}`);const s=r[0],n={exp:60,ext:{data:{pbadslot:i},gpid:i}};s?.params?.bidfloor&&(n.bidfloor=s.params.bidfloor,delete s.params.bidfloor),s?.params?.currency&&(n.bidfloorcur=s.params.currency,delete s.params.currency),oajs.addAdUnits({bids:r,mediaTypes:l,code:i,ortb2Imp:n})}})},I=(e=[])=>{if(window.globalAdConfig.isPrebidDisabled||document.visibilityState==="hidden")return Promise.resolve();let t=!1;return new Promise(o=>{pbjs.que.push(()=>{if(t)return o();t=!0;try{window.logAdEvent("Prebid: Request bids start. Ad units:",e),pbjs.requestBids({adUnitCodes:e,timeout:window.globalAdConfig.prebidTimeout,bidsBackHandler:i=>{window.logAdEvent("Prebid: Request bids complete"),o(i)}})}catch(i){console.error("Error pbjs.requestBids",i),o()}})})},C=(e=[])=>{if(window.globalAdConfig.isPrebidDisabled||!window.openAdsEnabled||document.visibilityState==="hidden")return Promise.resolve();let t=!1;return new Promise(o=>{oajs.que.push(()=>{if(t)return o();t=!0;try{window.logAdEvent("Open Ads: Request bids start"),oajs.requestBids({adUnitCodes:e,timeout:window.globalAdConfig.prebidTimeout,bidsBackHandler:i=>{window.logAdEvent("Open Ads: Request bids complete"),o(i)}})}catch(i){console.error("Error oajs.requestBids",i),o()}})})},G=(e,t)=>{const o=document.getElementById(e);o.innerHTML="";const i=t.width<=2||t.height<=2,a=document.createElement("iframe");i||(a.setAttribute("src","https://www.awxcdn.com/safeframe/1-0-0/html/container.html"),a.setAttribute("sandbox","allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation"),a.setAttribute("name",t.adId),a.setAttribute("height",t.height),a.setAttribute("width",t.width)),a.setAttribute("style","display:block;margin:auto"),a.setAttribute("frameborder",0),a.setAttribute("scrolling","no"),a.setAttribute("marginheight",0),a.setAttribute("marginwidth",0),a.setAttribute("TOPMARGIN",0),a.setAttribute("LEFTMARGIN",0),a.setAttribute("allowtransparency","true"),o.appendChild(a),i&&pbjs.renderAd(a.contentWindow.document,t.adId)};window.renderPrebidWithIframe=G;const ne=e=>{let t={cpm:0};return pbjs?.getBidResponsesForAdUnitCode&&pbjs.getBidResponsesForAdUnitCode(e).bids.forEach(i=>{F.indexOf(i.requestId)>-1&&i.cpm>t.cpm&&(t=i)}),t},ae=e=>{const{adUnitCode:t,adDivId:o}=e,i=ne(t);return i.cpm>0&&(googletag.pubads().setTargeting("pug","1"),window.globalAdConfig.buyItNowSkipGoogleAdManager)?(e.winner.auction=1,G(o,i),X({adUnitCode:t,adObject:e,customTargeting:i.adserverTargeting}),e.gptSlot=null,!0):!1},se=e=>{let t={upr:e.upr,upr_0:"no_bid",upr_auction:"skipped",hb_bid_1st:"no_bid",hb_bid_2nd:"no_bid"};if(pbjs?.getHighestCpmBids){const o=pbjs?.getHighestCpmBids?pbjs.getHighestCpmBids(e.adUnitCode):[],i=o.length&&o[0].cpm||0,d=i?(s=>s>15?"15.00":s>10?String(Math.round(s).toFixed(2)):String((Math.round(s*2)/2).toFixed(2)))(i):"no_bid";let l="no_bid",r="no_bid";if(pbjs?.getBidResponsesForAdUnitCode){const s=c=>(Math.round(c*10)/10).toFixed(2),n=pbjs.getBidResponsesForAdUnitCode(e.adUnitCode).bids;n.sort((c,p)=>p.cpm-c.cpm),n[0]&&(l=s(n[0].cpm)),n[1]&&(r=s(n[1].cpm))}t={upr:e.upr,upr_0:d,upr_auction:"prebid",userid3pbid:`${window.adInfo.userid3p}-${d}`,hb_bid_1st:l,hb_bid_2nd:r}}return t};window.getUprTargeting=se;const de=(e="")=>new Set(["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE","IS","LI","NO"]).has(e.toUpperCase()),re=({adSlots:e,userData:t})=>{if(t?.countryCode?.toLowerCase()!=="us")return;window.gameraFromPage=!0;let o="",i="",a="",d="",l=1;try{e&&(i=Object.values(e)[0].adUnitCode),o=window.RaineV2?.pageView?.pageInfo?.group||"",a=window?.adInfo?.partner||"accuweather",d=window?.adInfo?.wx_seg||"",l=1}catch(n){window.awxLogger?.withScope("Ads::setupGamera").debug("Error getting Gamera data from adSlots or window.adInfo",n)}window.gamera=window.gamera||{},window.gamera.cmd=window.gamera.cmd||[],window.gamera.cmd.push(function(){window.logAdEvent("Gamera initialized"),window.gamera.addDimensions({aw_site:i.split("/")[2],aw_wxGeo:i.split("/")[3],aw_page:o.replace("/",""),aw_partner:a,aw_wx_seg:d,aw_sub:window?.adInfo?.sub||""});try{let n=window?.gamera?.getUserMetrics()?.avg_cpm||void 0;n&&(n=(Math.round(n*20)/20).toFixed(2),window.adInfo.ucpm=n)}catch(n){window.awxLogger?.withScope("Ads::setupGamera").debug("Error getting ucpm from Gamera",n)}try{let n=window?.gamera?.getUserMetrics()?.avg_fillrate||void 0;n&&(n=(Math.round(n*20)/20).toString(),window.adInfo.ufill=n)}catch{}try{let n=window?.gamera?.getUserMetrics()?.visits||void 0;n&&(n.last_7&&(window.adInfo.uvisits_7=n.last_7.toString()),n.last_14&&(window.adInfo.uvisits_14=n.last_14.toString()),n.last_30&&(window.adInfo.uvisits_30=n.last_30.toString()),n.lifetime&&(window.adInfo.uvisits_life=n.lifetime.toString()))}catch{}try{let n=window?.gamera?.getOnPageSegments()?.filter(c=>!/^user_/.test(c)).join(",")||void 0;n&&(window.adInfo.cohort=n)}catch{}try{let n=window?.gamera?.getPrebidSegments()?.user?.data[0]?.segment?.map(c=>c.id).join(",")||void 0;n&&(window.adInfo.iabatax=n)}catch(n){window.awxLogger?.withScope("Ads::setupGamera").debug("Error getting cohort from Gamera",n)}});const r=document.createElement("script");r.setAttribute("id","__gamera__"),r.setAttribute("async","true"),r.src=`https://metrics.rapidedge.io/gamera.js?domain=accuweather.com&ltv=${l}&tpcs=1`;const s=document.getElementsByTagName("script")[0];s?s.parentNode.insertBefore(r,s):window.logAdEvent("Error adding Gamera script tag")},le=()=>{const e=googletag.pubads(),t=window.adInfo??{};for(const[o,i]of Object.entries(t)){if(i==null||i===""){e.clearTargeting(o);continue}const a=Array.isArray(i)?i.map(String):String(i),l=e.getTargeting(o).join("|"),r=Array.isArray(a)?a.join("|"):a;l!==r&&e.setTargeting(o,a)}},ce=()=>{window.globalAdConfig.disableInitialAdLoad&&googletag.pubads().disableInitialLoad(),window.globalAdConfig.gptEnableSingleRequest&&googletag.pubads().enableSingleRequest(),window.globalAdConfig.gptLazyLoading&&googletag.pubads().enableLazyLoad(window.globalAdConfig.gptLazyLoading),googletag.enableServices(),googletag.pubads().enableAsyncRendering(),googletag.pubads().setCentering(!0),googletag.pubads().setSafeFrameConfig({allowOverlayExpansion:!1,allowPushExpansion:!0,sandbox:!0});for(const[t,o]of Object.entries(window.adInfo))o&&googletag.pubads().setTargeting(t,o);typeof window.ketch=="function"?window.ketch("once","consent",t=>{googletag.pubads().setTargeting("optout",t?.purposes?.targeted_advertising?"false":"true")}):googletag.pubads().setTargeting("optout","false");const e=window.globalAdConfig.hashedEmail||window.globalAdConfig.ppid;if(e&&googletag.pubads().setPublisherProvidedId(e),window.globalAdConfig.userData?.zipCodes?.length>0&&window.globalAdConfig.userData?.countryCode?.toLowerCase()==="us"){const t=window.globalAdConfig.userData.zipCodes[0].primary;googletag.pubads().setLocation(`${t},US`)}};window.googletag=window.googletag||{cmd:[]};window.pbjs=window.pbjs||{};window.pbjs.que=window.pbjs.que||[];window.oajs=window.oajs||{};window.oajs.que=window.oajs.que||[];let _=!1;window.adTimeline=[];window.logAdEvent=e=>{new URLSearchParams(window.location.search).has("debug")&&console.debug(`Ad event: ${e}`),window.adTimeline.push([performance.now().toFixed(2),e])};document.addEventListener("DOMContentLoaded",()=>{window.logAdEvent("DOM Ready")});window.addEventListener("onAwxAppMounted",()=>{window.logAdEvent("App mounted")});const H=()=>{const e=window.location.pathname.replace("/app","").replaceAll("/","");return window.tagEngineDataLayer.features?.raineAdsTracking&&e==="today"},b=(e,t,o)=>{H()&&window.trackRaineEvent?.(`${window.globalAdConfig?.platform}_ads`,e,t,o)},L=()=>{H()&&window.sendGenericEvents?.(!0)};Z();const T=!!window.tagEngineDataLayer.adData||!!window.tagEngineDataLayer.adDataAdc;if(T){const e=M();J(e),z(e),$(e),re(e)}window.prebidTimeoutPromise=new Promise(e=>{if(!T||window.globalAdConfig.isPrebidDisabled)return Promise.resolve();pbjs.que.push(()=>{pbjs.onEvent("auctionInit",()=>{setTimeout(e,window.globalAdConfig?.prebidTimeout)})})});const P=new Set,V=()=>!!window.globalAdConfig?.gptLazyLoading&&!window.globalAdConfig?.gptEnableSingleRequest,ge=()=>`${(window.globalAdConfig?.gptLazyLoading?.fetchMarginPercent??0)*2}% 0px`;let y=null;const pe=()=>{if(y)return y;const e=ge();return window.logAdEvent(`Lazy auction observer: rootMargin=${e}`),y=new IntersectionObserver(t=>{t.forEach(o=>{if(!o.isIntersecting)return;const i=o.target.id,a=Array.from(window.adsOnPage.values()).find(r=>r.adDivId===i);if(!a)return;const{adUnitCode:d,gptSlot:l}=a;P.has(d)||(P.add(d),y.unobserve(o.target),window.logAdEvent(`Lazy auction: fetching bids for ${i}`),Promise.all([I([d]),C([d])]).then(()=>{if(!l)return;const r=pbjs.getHighestCpmBids?.(d)||[],s=oajs.getHighestCpmBids?.(d)||[],c=[...r,...s].reduce((p,g)=>g.cpm>(p?.cpm??0)?g:p,null);if(c?.adserverTargeting){const p={...c.adserverTargeting};for(const[g,w]of Object.entries(p))typeof w=="string"&&w.includes(",")?p[g]=w.split(","):typeof w=="number"&&(p[g]=String(w));["bidder","size","pb"].forEach(g=>{const w=`oa_${g}`,f=`hb_${g}`;p[w]&&(p[f]=p[w])}),window.logAdEvent(`Lazy auction: set targeting for ${i} - ${JSON.stringify(p)}`),l.setConfig({targeting:p})}}))})},{rootMargin:e}),y},ue=()=>{y&&(y.disconnect(),y=null),P.clear()},K=()=>{if(V()){const e=Array.from(window.adsOnPage.values()).filter(t=>t.adDivId.includes("top")||t.adDivId.includes("adhesion")).map(t=>t.adUnitCode);return Promise.all([I(e),C(e)])}else return Promise.all([I(),C()])};W().then(()=>{if(!T)return;window.logAdEvent("Starting ad process");const e=oe();pbjs.que.push(()=>{window.logAdEvent("Prebid: Init"),ie(e),k()}),oajs.que.push(()=>{window.logAdEvent("OpenAds: Init"),oajs.setConfig({...e,s2sConfig:{accountId:"accuweather",bidders:["thetradedesk"],enabled:!0,endpoint:"https://openads.adsrvr.org/openrtb2/auction",syncEndpoint:"https://openads.adsrvr.org/cookie_sync",timeout:window.globalAdConfig.prebidTimeout}}),N()}),window.initialAuctionsPromise=K(),googletag.cmd.push(()=>{window.logAdEvent("GPT: Init"),ce(),googletag.pubads().addEventListener("slotResponseReceived",i=>{const a=i.slot.getSlotElementId();if(a.includes("top")){const d=document.getElementById(a),l=d.getBoundingClientRect(),r=window.getComputedStyle(d);b("top_ad_slotResponseReceived"),b("top_ad_propsOnRespReceived","divSize",`${l.width}x${l.height}`),b("top_ad_propsOnRespReceived","divDisplay",r.display),b("top_ad_propsOnRespReceived","divVisibility",r.visibility),b("top_ad_propsOnRespReceived","divOpacity",r.opacity),b("top_ad_propsOnRespReceived","hasHiddenAncestor",`${fe(d)}`),b("top_ad_propsOnRespReceived","visibilityState",document.visibilityState),L()}}),googletag.pubads().addEventListener("slotRenderEnded",i=>{const a=i.slot.getSlotElementId();if(a.includes("top")){b("top_ad_slotRenderEnded"),b("top_ad_propsOnRenderEnded","isEmpty",`${i.isEmpty}`),b("top_ad_propsOnRenderEnded","visibilityState",document.visibilityState);const d=document.getElementById(a);if(!d)b("top_ad_propsOnRenderEnded","divNotFound");else{const l=d.getBoundingClientRect();b("top_ad_propsOnRenderEnded","divSize",`${l.width}x${l.height}`)}L()}});let t=!1;const o=()=>{if(t)return;t=!0;const i=document.querySelector(".app.loaded"),a=window.tagEngineDataLayer?.adDataAdc;i||a?R():window.addEventListener("onAwxAppMounted",R)};window.globalAdConfig.disableInitialAdLoad?(setTimeout(o,window.globalAdConfig.awxTimeout),window.initialAuctionsPromise.then(o)):o(),googletag.pubads().addEventListener("slotResponseReceived",()=>{if(!_&&window.adsOnPage.has("interstitial")){_=!0;const{gptSlot:i}=window.adsOnPage.get("interstitial");i&&(googletag.display(i.getSlotElementId()),googletag.pubads().refresh([i]))}})})});const we=(e,t)=>{window.dispatchEvent(new CustomEvent("adsReload"));const o=M(e);o?.adSlots&&(_=!1,ue(),z(o),googletag.cmd.push(le),$(o),k(),N(),K().then(()=>{if(t){const a=googletag.pubads().getSlots().filter(d=>Object.keys(o.adSlots).includes(d.getSlotElementId()));a.length>0&&googletag.destroySlots(a)}else googletag.destroySlots();R()}))};let x;window.reloadAds=(e,t)=>{x&&clearTimeout(x),x=setTimeout(()=>{x=void 0,we(e,t)},100)};const R=()=>{window.dispatchEvent(new CustomEvent("refreshAdsOnPage"));const o=window.location.pathname.toLowerCase().replace("/app","").replaceAll("/","")==="today"&&window.globalAdConfig.gptEnableSingleRequest&&!!window.globalAdConfig.gptLazyLoading,i=[],a=[];window.adsOnPage.forEach(n=>{if(!document.getElementById(n?.adDivId)){window.logAdEvent(`Unable to find ad div for: ${n?.adDivId}`),n?.adDivId?.includes("top")&&(b("top_ad_slot_not_found_before_display"),L());return}const{sizes:c,adDivId:p,slot:g}=n;if(ae(n))return;let f;if(g==="oop"?f=googletag.defineOutOfPageSlot(n.adUnitCode,p):g==="interstitial"?f=googletag.defineOutOfPageSlot(n.adUnitCode,googletag.enums.OutOfPageFormat.INTERSTITIAL):f=googletag.defineSlot(n.adUnitCode,c,p),f){n.gptSlot=f,f.addService(googletag.pubads()),window.logAdEvent(`GPT: Display: ${p}`),googletag.display(f);for(const[m,u]of Object.entries(window.getUprTargeting(n)))u&&f.setTargeting(m,String(u));try{window.gamera._getAdPlacements().forEach(({divId:m,universalPlacementId:u})=>{m===n.adDivId&&u&&f.setTargeting("upid",u)})}catch{}if(V()&&!["interstitial","preroll","oop","adhesion","top"].includes(g)){const m=document.getElementById(p);m&&(pe().observe(m),window.logAdEvent(`Lazy auction: observing ${p}`))}g!=="interstitial"&&g!=="preroll"&&(o&&(p?.includes("middle")||p?.includes("bottom"))?a.push(f):i.push(f))}});const d=pbjs.getHighestCpmBids?.()||[],l=oajs.getHighestCpmBids?.()||[],r=[...d,...l],s=new Map;r.forEach(n=>{const c=s.get(n.adUnitCode);(!c||n.cpm>c.cpm)&&s.set(n.adUnitCode,n)}),s.forEach(n=>{const c=Array.from(window.adsOnPage.values()).find(p=>p.adUnitCode===n.adUnitCode);if(c?.gptSlot){const{adserverTargeting:p}=n;for(const[g,w]of Object.entries(p))typeof w=="string"&&w.includes(",")?p[g]=w.split(","):typeof w=="number"&&(p[g]=String(w));["bidder","size","pb"].forEach(g=>{const w=`oa_${g}`,f=`hb_${g}`;p[w]&&(p[f]=p[w])}),window.logAdEvent(`GPT: Set targeting for ${c.adDivId} - ${JSON.stringify(p)}`),c.gptSlot.setConfig({targeting:p})}}),window.globalAdConfig.disableInitialAdLoad&&document.visibilityState==="visible"&&(window.logAdEvent("GPT: Refresh"),o?(i.length&&googletag.pubads().refresh(i),a.length&&googletag.pubads().refresh(a)):window.globalAdConfig.gptEnableSingleRequest?googletag.pubads().refresh(i):i.forEach(n=>{googletag.pubads().refresh([n])}))};function fe(e){for(;e;){const t=window.getComputedStyle(e);if(t.display==="none"||t.visibility==="hidden"||t.opacity==="0")return!0;e=e.parentElement}return!1}
//# sourceMappingURL=gpt-script.inline-d59b417c.js.map
})();</script><script async="" src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>

	

	<script>
function getAwxSession(categories, pageId) {
	const AWX_SESSION_NAME = 'awx_session';
	const defaultVal = {
		categoryFlow: [],
		visitFlow: [],
		ttl: Date.now() + 600000
	};

	let awxSession = JSON.parse(window.localStorage.getItem(AWX_SESSION_NAME) || '{}');
	if (!awxSession.ttl || Date.now() > awxSession.ttl) {
		awxSession = defaultVal;
	}

	if (categories) {
		categories = categories.toLowerCase().replace(/\s/g, '-');
		awxSession.categoryFlow = awxSession.categoryFlow.concat(categories.split('|')).slice(-30);
	}

	if (pageId) {
		awxSession.visitFlow.push(pageId);
	}

	try {
		window.localStorage.setItem(AWX_SESSION_NAME, JSON.stringify(awxSession));
	} catch {};

	return {
		categoryFlow: awxSession.categoryFlow.join('/'),
		visitFlow: awxSession.visitFlow.join('/'),
		visitFlowArray: awxSession.visitFlow
	};
}

function getUserContentAffinity(categories) {
	const storageKey = 'awxContentAffinity';
	const storageValue = window.localStorage.getItem(storageKey);
	const contentAffinity = (storageValue && storageValue !== '{}') ? JSON.parse(storageValue) : window.userCookie.userContentAffinity;

	if (categories) {
		categories = categories.toLowerCase().replace(/\s/g, '-');
		categories.split('|').forEach(function(category) {
			contentAffinity[category] = (contentAffinity[category] || 0) + 1;
		});
	}

	try {
		window.localStorage.setItem(storageKey, JSON.stringify(contentAffinity));
	} catch {};

	return Object.keys(contentAffinity).map(function(category) {
		return category + ':' + contentAffinity[category];
	}).join('/');
}
</script>

	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag() { dataLayer.push(arguments); }
	</script>
				<link rel="stylesheet" href="https://www.awxcdn.com/adc-assets/bundles/city.three-day-desktop.aba4addc70757dd0c0a5.css">
		<link rel="stylesheet" href="https://www.awxcdn.com/adc-assets/bundles/4207.67441d56684b2bca10e9.css">

				<link rel="stylesheet" href="https://www.awxcdn.com/adc-assets/bundles/legacy-header.db68efe94cf86bd9e422.css">


	<script>
	(function () {
		const COOKIE_NAME = 'tag-preview';
		const COOKIE_DURATION_MINUTES = 10;

		function setCookie(name, value, minutes) {
			const expires = new Date(Date.now() + minutes * 60000).toUTCString();
			document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
		}

		function deleteCookie(name) {
			document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
		}

		function getQueryParam(param) {
			const params = new URLSearchParams(window.location.search);
			return params.get(param);
		}

		const previewParam = getQueryParam(COOKIE_NAME);

		if (previewParam !== null) {
			if (previewParam.trim() === '') {
				deleteCookie(COOKIE_NAME);
			} else {
				setCookie(COOKIE_NAME, previewParam, COOKIE_DURATION_MINUTES);
			}
		}
	})();
</script>


	
<script>bazadebezolkohpepadr="364973853"</script><script type="text/javascript" src="https://www.accuweather.com/akam/13/15c10ccf" defer=""></script><script type="text/javascript" async="" defer="" src="https://cdn.ketchjs.com/ketchtag/stable/v2.12/ketch-sdk.js"></script><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9nrunKdU5m96PSN1XsSGr3qOP0lvPFUB2AiAylCDlN5DTl17uDFkpQuHj1AFtgWLxpLaiBZuhrtb2WOu7ofHwEAAACKeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiQUlQcm9tcHRBUElNdWx0aW1vZGFsSW5wdXQiLCJleHBpcnkiOjE3NzQzMTA0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A93bovR+QVXNx2/38qDbmeYYf1wdte9EO37K9eMq3r+541qo0byhYU899BhPB7Cv9QqD7wIbR1B6OAc9kEfYCA4AAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiQUlQcm9tcHRBUElNdWx0aW1vZGFsSW5wdXQiLCJleHBpcnkiOjE3NzQzMTA0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A1S5fojrAunSDrFbD8OfGmFHdRFZymSM/1ss3G+NEttCLfHkXvlcF6LGLH8Mo5PakLO1sCASXU1/gQf6XGuTBgwAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQUlQcm9tcHRBUElNdWx0aW1vZGFsSW5wdXQiLCJleHBpcnkiOjE3NzQzMTA0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script src="https://securepubads.g.doubleclick.net/pagead/managed/js/gpt/m202604140101/pubads_impl.js?cb=31097937" async=""></script><style>#lanyard_root {
  *, ::before, ::after {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x:  ;
    --tw-pan-y:  ;
    --tw-pinch-zoom:  ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position:  ;
    --tw-gradient-via-position:  ;
    --tw-gradient-to-position:  ;
    --tw-ordinal:  ;
    --tw-slashed-zero:  ;
    --tw-numeric-figure:  ;
    --tw-numeric-spacing:  ;
    --tw-numeric-fraction:  ;
    --tw-ring-inset:  ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgb(59 130 246 / 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur:  ;
    --tw-brightness:  ;
    --tw-contrast:  ;
    --tw-grayscale:  ;
    --tw-hue-rotate:  ;
    --tw-invert:  ;
    --tw-saturate:  ;
    --tw-sepia:  ;
    --tw-drop-shadow:  ;
    --tw-backdrop-blur:  ;
    --tw-backdrop-brightness:  ;
    --tw-backdrop-contrast:  ;
    --tw-backdrop-grayscale:  ;
    --tw-backdrop-hue-rotate:  ;
    --tw-backdrop-invert:  ;
    --tw-backdrop-opacity:  ;
    --tw-backdrop-saturate:  ;
    --tw-backdrop-sepia:  ;
    --tw-contain-size:  ;
    --tw-contain-layout:  ;
    --tw-contain-paint:  ;
    --tw-contain-style:  ;
  }
  ::backdrop {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x:  ;
    --tw-pan-y:  ;
    --tw-pinch-zoom:  ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position:  ;
    --tw-gradient-via-position:  ;
    --tw-gradient-to-position:  ;
    --tw-ordinal:  ;
    --tw-slashed-zero:  ;
    --tw-numeric-figure:  ;
    --tw-numeric-spacing:  ;
    --tw-numeric-fraction:  ;
    --tw-ring-inset:  ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgb(59 130 246 / 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur:  ;
    --tw-brightness:  ;
    --tw-contrast:  ;
    --tw-grayscale:  ;
    --tw-hue-rotate:  ;
    --tw-invert:  ;
    --tw-saturate:  ;
    --tw-sepia:  ;
    --tw-drop-shadow:  ;
    --tw-backdrop-blur:  ;
    --tw-backdrop-brightness:  ;
    --tw-backdrop-contrast:  ;
    --tw-backdrop-grayscale:  ;
    --tw-backdrop-hue-rotate:  ;
    --tw-backdrop-invert:  ;
    --tw-backdrop-opacity:  ;
    --tw-backdrop-saturate:  ;
    --tw-backdrop-sepia:  ;
    --tw-contain-size:  ;
    --tw-contain-layout:  ;
    --tw-contain-paint:  ;
    --tw-contain-style:  ;
  }
}
#lanyard_root * .ketch-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
#lanyard_root * .ketch-pointer-events-none {
  pointer-events: none;
}
#lanyard_root * .ketch-pointer-events-auto {
  pointer-events: auto;
}
#lanyard_root * .ketch-fixed {
  position: fixed;
}
#lanyard_root * .ketch-absolute {
  position: absolute;
}
#lanyard_root * .ketch-relative {
  position: relative;
}
#lanyard_root * .ketch-inset-0 {
  inset: 0;
}
#lanyard_root * .ketch-inset-y-0 {
  top: 0;
  bottom: 0;
}
#lanyard_root * .\!ketch-left-0 {
  left: 0 !important;
}
#lanyard_root * .\!ketch-right-0 {
  right: 0 !important;
}
#lanyard_root * .ketch-bottom-0 {
  bottom: 0;
}
#lanyard_root * .ketch-bottom-1 {
  bottom: 4px;
}
#lanyard_root * .ketch-bottom-2\/4 {
  bottom: 50%;
}
#lanyard_root * .ketch-bottom-\[50\%\] {
  bottom: 50%;
}
#lanyard_root * .ketch-bottom-auto {
  bottom: auto;
}
#lanyard_root * .ketch-end-\[2px\] {
  inset-inline-end: 2px;
}
#lanyard_root * .ketch-left-0 {
  left: 0;
}
#lanyard_root * .ketch-left-1 {
  left: 4px;
}
#lanyard_root * .ketch-left-auto {
  left: auto;
}
#lanyard_root * .ketch-right-0 {
  right: 0;
}
#lanyard_root * .ketch-right-1 {
  right: 4px;
}
#lanyard_root * .ketch-start-\[2px\] {
  inset-inline-start: 2px;
}
#lanyard_root * .ketch-top-0 {
  top: 0;
}
#lanyard_root * .ketch-top-1 {
  top: 4px;
}
#lanyard_root * .ketch-top-\[2px\] {
  top: 2px;
}
#lanyard_root * .ketch-top-\[4px\] {
  top: 4px;
}
#lanyard_root * .-ketch-z-10 {
  z-index: -10;
}
#lanyard_root * .ketch-z-0 {
  z-index: 0;
}
#lanyard_root * .ketch-z-10 {
  z-index: 10;
}
#lanyard_root * .ketch-z-ketch-max-z-index {
  z-index: 2147483647;
}
#lanyard_root * .ketch-col-span-1 {
  grid-column: span 1 / span 1;
}
#lanyard_root * .ketch-col-span-12 {
  grid-column: span 12 / span 12;
}
#lanyard_root * .ketch-col-span-2 {
  grid-column: span 2 / span 2;
}
#lanyard_root * .ketch-row-span-1 {
  grid-row: span 1 / span 1;
}
#lanyard_root * .\!ketch-m-0 {
  margin: 0 !important;
}
#lanyard_root * .ketch-m-0 {
  margin: 0;
}
#lanyard_root * .ketch-mx-16 {
  margin-left: 64px;
  margin-right: 64px;
}
#lanyard_root * .ketch-mx-auto {
  margin-left: auto;
  margin-right: auto;
}
#lanyard_root * .ketch-my-0 {
  margin-top: 0;
  margin-bottom: 0;
}
#lanyard_root * .ketch-my-2 {
  margin-top: 8px;
  margin-bottom: 8px;
}
#lanyard_root * .ketch-my-4 {
  margin-top: 16px;
  margin-bottom: 16px;
}
#lanyard_root * .ketch-mb-1 {
  margin-bottom: 4px;
}
#lanyard_root * .ketch-mb-2 {
  margin-bottom: 8px;
}
#lanyard_root * .ketch-mb-3 {
  margin-bottom: 12px;
}
#lanyard_root * .ketch-mb-4 {
  margin-bottom: 16px;
}
#lanyard_root * .ketch-mb-6 {
  margin-bottom: 24px;
}
#lanyard_root * .ketch-mb-8 {
  margin-bottom: 32px;
}
#lanyard_root * .ketch-ml-0 {
  margin-left: 0;
}
#lanyard_root * .ketch-ml-1 {
  margin-left: 4px;
}
#lanyard_root * .ketch-ml-2\.5 {
  margin-left: 10px;
}
#lanyard_root * .ketch-ml-4 {
  margin-left: 16px;
}
#lanyard_root * .ketch-ml-\[18px\] {
  margin-left: 18px;
}
#lanyard_root * .ketch-ml-\[24px\] {
  margin-left: 24px;
}
#lanyard_root * .ketch-ml-auto {
  margin-left: auto;
}
#lanyard_root * .ketch-mr-4 {
  margin-right: 16px;
}
#lanyard_root * .ketch-mr-auto {
  margin-right: auto;
}
#lanyard_root * .ketch-mt-1 {
  margin-top: 4px;
}
#lanyard_root * .ketch-mt-3 {
  margin-top: 12px;
}
#lanyard_root * .ketch-mt-4 {
  margin-top: 16px;
}
#lanyard_root * .ketch-mt-5 {
  margin-top: 20px;
}
#lanyard_root * .ketch-mt-8 {
  margin-top: 32px;
}
#lanyard_root * .ketch-box-border {
  box-sizing: border-box;
}
#lanyard_root * .\!ketch-block {
  display: block !important;
}
#lanyard_root * .ketch-block {
  display: block;
}
#lanyard_root * .ketch-inline-block {
  display: inline-block;
}
#lanyard_root * .ketch-inline {
  display: inline;
}
#lanyard_root * .\!ketch-flex {
  display: flex !important;
}
#lanyard_root * .ketch-flex {
  display: flex;
}
#lanyard_root * .ketch-inline-flex {
  display: inline-flex;
}
#lanyard_root * .ketch-grid {
  display: grid;
}
#lanyard_root * .ketch-hidden {
  display: none;
}
#lanyard_root * .ketch-aspect-\[1024\/480\] {
  aspect-ratio: 1024/480;
}
#lanyard_root * .ketch-h-0 {
  height: 0;
}
#lanyard_root * .ketch-h-10 {
  height: 40px;
}
#lanyard_root * .ketch-h-11 {
  height: 44px;
}
#lanyard_root * .ketch-h-12 {
  height: 48px;
}
#lanyard_root * .ketch-h-16 {
  height: 64px;
}
#lanyard_root * .ketch-h-24 {
  height: 96px;
}
#lanyard_root * .ketch-h-4 {
  height: 16px;
}
#lanyard_root * .ketch-h-5 {
  height: 20px;
}
#lanyard_root * .ketch-h-6 {
  height: 24px;
}
#lanyard_root * .ketch-h-9 {
  height: 36px;
}
#lanyard_root * .ketch-h-\[17px\] {
  height: 17px;
}
#lanyard_root * .ketch-h-\[20px\] {
  height: 20px;
}
#lanyard_root * .ketch-h-\[22px\] {
  height: 22px;
}
#lanyard_root * .ketch-h-\[30px\] {
  height: 30px;
}
#lanyard_root * .ketch-h-\[50\%\] {
  height: 50%;
}
#lanyard_root * .ketch-h-auto {
  height: auto;
}
#lanyard_root * .ketch-h-dvh {
  height: 100dvh;
}
#lanyard_root * .ketch-h-full {
  height: 100%;
}
#lanyard_root * .ketch-h-px {
  height: 1px;
}
#lanyard_root * .ketch-max-h-10 {
  max-height: 40px;
}
#lanyard_root * .ketch-max-h-44 {
  max-height: 176px;
}
#lanyard_root * .ketch-max-h-6 {
  max-height: 24px;
}
#lanyard_root * .ketch-max-h-60 {
  max-height: 240px;
}
#lanyard_root * .ketch-max-h-9 {
  max-height: 36px;
}
#lanyard_root * .ketch-max-h-\[30px\] {
  max-height: 30px;
}
#lanyard_root * .ketch-max-h-\[48px\] {
  max-height: 48px;
}
#lanyard_root * .ketch-max-h-\[64px\] {
  max-height: 64px;
}
#lanyard_root * .ketch-max-h-\[69px\] {
  max-height: 69px;
}
#lanyard_root * .ketch-max-h-\[75\%\] {
  max-height: 75%;
}
#lanyard_root * .ketch-max-h-\[90\%\] {
  max-height: 90%;
}
#lanyard_root * .ketch-max-h-dvh {
  max-height: 100dvh;
}
#lanyard_root * .ketch-max-h-full {
  max-height: 100%;
}
#lanyard_root * .ketch-min-h-0 {
  min-height: 0;
}
#lanyard_root * .ketch-min-h-10 {
  min-height: 40px;
}
#lanyard_root * .ketch-min-h-11 {
  min-height: 44px;
}
#lanyard_root * .ketch-min-h-12 {
  min-height: 48px;
}
#lanyard_root * .ketch-min-h-7 {
  min-height: 28px;
}
#lanyard_root * .ketch-min-h-8 {
  min-height: 32px;
}
#lanyard_root * .ketch-min-h-\[125px\] {
  min-height: 125px;
}
#lanyard_root * .ketch-min-h-\[57px\] {
  min-height: 57px;
}
#lanyard_root * .ketch-min-h-\[75px\] {
  min-height: 75px;
}
#lanyard_root * .ketch-min-h-full {
  min-height: 100%;
}
#lanyard_root * .ketch-min-h-lvh {
  min-height: 100lvh;
}
#lanyard_root * .\!ketch-w-full {
  width: 100% !important;
}
#lanyard_root * .ketch-w-10 {
  width: 40px;
}
#lanyard_root * .ketch-w-11 {
  width: 44px;
}
#lanyard_root * .ketch-w-16 {
  width: 64px;
}
#lanyard_root * .ketch-w-24 {
  width: 96px;
}
#lanyard_root * .ketch-w-4 {
  width: 16px;
}
#lanyard_root * .ketch-w-48 {
  width: 192px;
}
#lanyard_root * .ketch-w-5 {
  width: 20px;
}
#lanyard_root * .ketch-w-6 {
  width: 24px;
}
#lanyard_root * .ketch-w-9 {
  width: 36px;
}
#lanyard_root * .ketch-w-\[115px\] {
  width: 115px;
}
#lanyard_root * .ketch-w-\[134px\] {
  width: 134px;
}
#lanyard_root * .ketch-w-\[224px\] {
  width: 224px;
}
#lanyard_root * .ketch-w-\[30px\] {
  width: 30px;
}
#lanyard_root * .ketch-w-\[328px\] {
  width: 328px;
}
#lanyard_root * .ketch-w-\[calc\(100\%-8px\)\] {
  width: calc(100% - 8px);
}
#lanyard_root * .ketch-w-auto {
  width: auto;
}
#lanyard_root * .ketch-w-fit {
  width: -moz-fit-content;
  width: fit-content;
}
#lanyard_root * .ketch-w-full {
  width: 100%;
}
#lanyard_root * .ketch-w-px {
  width: 1px;
}
#lanyard_root * .ketch-min-w-0 {
  min-width: 0;
}
#lanyard_root * .ketch-min-w-10 {
  min-width: 40px;
}
#lanyard_root * .ketch-min-w-5 {
  min-width: 20px;
}
#lanyard_root * .ketch-min-w-\[484px\] {
  min-width: 484px;
}
#lanyard_root * .ketch-min-w-full {
  min-width: 100%;
}
#lanyard_root * .ketch-max-w-5xl {
  max-width: 64rem;
}
#lanyard_root * .ketch-max-w-6 {
  max-width: 24px;
}
#lanyard_root * .ketch-max-w-9 {
  max-width: 36px;
}
#lanyard_root * .ketch-max-w-\[140px\] {
  max-width: 140px;
}
#lanyard_root * .ketch-max-w-\[200px\] {
  max-width: 200px;
}
#lanyard_root * .ketch-max-w-\[268px\] {
  max-width: 268px;
}
#lanyard_root * .ketch-max-w-\[30px\] {
  max-width: 30px;
}
#lanyard_root * .ketch-max-w-\[400px\] {
  max-width: 400px;
}
#lanyard_root * .ketch-max-w-\[560px\] {
  max-width: 560px;
}
#lanyard_root * .ketch-max-w-full {
  max-width: 100%;
}
#lanyard_root * .ketch-max-w-md {
  max-width: 28rem;
}
#lanyard_root * .ketch-max-w-none {
  max-width: none;
}
#lanyard_root * .ketch-flex-1 {
  flex: 1 1 0%;
}
#lanyard_root * .ketch-flex-shrink-0 {
  flex-shrink: 0;
}
#lanyard_root * .ketch-shrink {
  flex-shrink: 1;
}
#lanyard_root * .ketch-shrink-0 {
  flex-shrink: 0;
}
#lanyard_root * .ketch-flex-grow {
  flex-grow: 1;
}
#lanyard_root * .ketch-flex-grow-0 {
  flex-grow: 0;
}
#lanyard_root * .ketch-grow {
  flex-grow: 1;
}
#lanyard_root * .ketch-grow-0 {
  flex-grow: 0;
}
#lanyard_root * .ketch-border-collapse {
  border-collapse: collapse;
}
#lanyard_root * .ketch-translate-y-2\/4 {
  --tw-translate-y: 50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
#lanyard_root * .ketch-translate-y-\[50\%\] {
  --tw-translate-y: 50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
@keyframes ketch-backdropFadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
#lanyard_root * .ketch-animate-backdropFadeOut {
  animation: ketch-backdropFadeOut 0.4s forwards;
}
@keyframes ketch-bannerAnimateCenter {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
#lanyard_root * .ketch-animate-bannerAnimateCenter {
  animation: ketch-bannerAnimateCenter 0.4s forwards;
}
@keyframes ketch-bannerAnimateTop {
  from {
    transform: translateY(-900px);
  }
  to {
    transform: translateY(0);
  }
}
#lanyard_root * .ketch-animate-bannerAnimateTop {
  animation: ketch-bannerAnimateTop 0.4s forwards;
}
@keyframes ketch-bannerDesktopAnimate {
  from {
    transform: translateY(900px);
  }
  to {
    transform: translateY(0);
  }
}
#lanyard_root * .ketch-animate-bannerDesktopAnimate {
  animation: ketch-bannerDesktopAnimate 0.4s forwards;
}
@keyframes ketch-bannerDismissBottom {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(900px);
  }
}
#lanyard_root * .ketch-animate-bannerDismissBottom {
  animation: ketch-bannerDismissBottom 0.4s forwards;
}
@keyframes ketch-bannerDismissCenter {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
#lanyard_root * .ketch-animate-bannerDismissCenter {
  animation: ketch-bannerDismissCenter 0.4s forwards;
}
@keyframes ketch-bannerMobileBottomAnimate {
  from {
    transform: translateY(900px);
  }
  to {
    transform: translateY(0);
  }
}
#lanyard_root * .ketch-animate-bannerMobileBottomAnimate {
  animation: ketch-bannerMobileBottomAnimate 0.4s forwards;
}
@keyframes ketch-bannerMobileDismissBottom {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(900px);
  }
}
#lanyard_root * .ketch-animate-bannerMobileDismissBottom {
  animation: ketch-bannerMobileDismissBottom 0.4s forwards;
}
@keyframes ketch-fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
#lanyard_root * .ketch-animate-fadeIn {
  animation: ketch-fadeIn 0.5s ease-in-out;
}
@keyframes ketch-modalAnimatedLeft {
  from {
    left: -900px;
  }
  to {
    left: 4px;
  }
}
#lanyard_root * .ketch-animate-modalAnimatedLeft {
  animation: ketch-modalAnimatedLeft 0.4s forwards;
}
@keyframes ketch-modalAnimatedRight {
  from {
    right: -900px;
  }
  to {
    right: 4px;
  }
}
#lanyard_root * .ketch-animate-modalAnimatedRight {
  animation: ketch-modalAnimatedRight 0.4s forwards;
}
#lanyard_root * .ketch-animate-none {
  animation: none;
}
@keyframes ketch-pulseOpacity {
  0%, 100% {
    opacity: 0.3;
  }
  50% {
    opacity: 1;
  }
}
#lanyard_root * .ketch-animate-pulseOpacity {
  animation: ketch-pulseOpacity 2s ease-in-out infinite;
}
#lanyard_root * .ketch-cursor-default {
  cursor: default;
}
#lanyard_root * .ketch-cursor-pointer {
  cursor: pointer;
}
#lanyard_root * .ketch-resize-none {
  resize: none;
}
#lanyard_root * .ketch-list-disc {
  list-style-type: disc;
}
#lanyard_root * .ketch-list-none {
  list-style-type: none;
}
#lanyard_root * .ketch-appearance-none {
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
}
#lanyard_root * .ketch-auto-rows-min {
  grid-auto-rows: min-content;
}
#lanyard_root * .ketch-grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}
#lanyard_root * .ketch-grid-cols-12 {
  grid-template-columns: repeat(12, minmax(0, 1fr));
}
#lanyard_root * .ketch-grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
#lanyard_root * .ketch-grid-rows-1 {
  grid-template-rows: repeat(1, minmax(0, 1fr));
}
#lanyard_root * .ketch-grid-rows-\[auto_auto_1fr\] {
  grid-template-rows: auto auto 1fr;
}
#lanyard_root * .ketch-flex-row {
  flex-direction: row;
}
#lanyard_root * .ketch-flex-col {
  flex-direction: column;
}
#lanyard_root * .ketch-flex-col-reverse {
  flex-direction: column-reverse;
}
#lanyard_root * .ketch-flex-wrap {
  flex-wrap: wrap;
}
#lanyard_root * .ketch-items-start {
  align-items: flex-start;
}
#lanyard_root * .ketch-items-end {
  align-items: flex-end;
}
#lanyard_root * .\!ketch-items-center {
  align-items: center !important;
}
#lanyard_root * .ketch-items-center {
  align-items: center;
}
#lanyard_root * .ketch-items-stretch {
  align-items: stretch;
}
#lanyard_root * .\!ketch-justify-start {
  justify-content: flex-start !important;
}
#lanyard_root * .ketch-justify-end {
  justify-content: flex-end;
}
#lanyard_root * .ketch-justify-center {
  justify-content: center;
}
#lanyard_root * .\!ketch-justify-between {
  justify-content: space-between !important;
}
#lanyard_root * .ketch-justify-between {
  justify-content: space-between;
}
#lanyard_root * .ketch-justify-stretch {
  justify-content: stretch;
}
#lanyard_root * .ketch-justify-items-center {
  justify-items: center;
}
#lanyard_root * .ketch-gap-0 {
  gap: 0;
}
#lanyard_root * .ketch-gap-1 {
  gap: 4px;
}
#lanyard_root * .ketch-gap-1\.5 {
  gap: 6px;
}
#lanyard_root * .ketch-gap-12 {
  gap: 48px;
}
#lanyard_root * .ketch-gap-16 {
  gap: 64px;
}
#lanyard_root * .ketch-gap-2 {
  gap: 8px;
}
#lanyard_root * .ketch-gap-3 {
  gap: 12px;
}
#lanyard_root * .ketch-gap-4 {
  gap: 16px;
}
#lanyard_root * .ketch-gap-5 {
  gap: 20px;
}
#lanyard_root * .ketch-gap-6 {
  gap: 24px;
}
#lanyard_root * .ketch-gap-8 {
  gap: 32px;
}
#lanyard_root * .ketch-gap-\[-2px\] {
  gap: -2px;
}
#lanyard_root * .ketch-gap-x-6 {
  -moz-column-gap: 24px;
       column-gap: 24px;
}
#lanyard_root * .ketch-gap-y-4 {
  row-gap: 16px;
}
#lanyard_root * :is(.ketch-space-x-1 > :not([hidden]) ~ :not([hidden])) {
  --tw-space-x-reverse: 0;
  margin-right: calc(4px * var(--tw-space-x-reverse));
  margin-left: calc(4px * calc(1 - var(--tw-space-x-reverse)));
}
#lanyard_root * .ketch-self-start {
  align-self: flex-start;
}
#lanyard_root * .ketch-overflow-auto {
  overflow: auto;
}
#lanyard_root * .ketch-overflow-hidden {
  overflow: hidden;
}
#lanyard_root * .ketch-overflow-y-auto {
  overflow-y: auto;
}
#lanyard_root * .ketch-overflow-y-scroll {
  overflow-y: scroll;
}
#lanyard_root * .ketch-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
#lanyard_root * .ketch-whitespace-nowrap {
  white-space: nowrap;
}
#lanyard_root * .ketch-whitespace-break-spaces {
  white-space: break-spaces;
}
#lanyard_root * .ketch-break-words {
  overflow-wrap: break-word;
}
#lanyard_root * .\!ketch-rounded-\[--k-banner-buttons-primary-cornerRadius\] {
  border-radius: var(--k-banner-buttons-primary-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-banner-buttons-secondary-cornerRadius\] {
  border-radius: var(--k-banner-buttons-secondary-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-banner-buttons-tertiary-cornerRadius\] {
  border-radius: var(--k-banner-buttons-tertiary-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-banner-container-cornerRadius\] {
  border-radius: var(--k-banner-container-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-banner-gpcBanner-cornerRadius\] {
  border-radius: var(--k-banner-gpcBanner-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-banner-header-returnButton-cornerRadius\] {
  border-radius: var(--k-banner-header-returnButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-actionBlock-button-cornerRadius\] {
  border-radius: var(--k-consentGate-actionBlock-button-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-consentBlock-button-cornerRadius\] {
  border-radius: var(--k-consentGate-consentBlock-button-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-cornerRadius\] {
  border-radius: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-cornerRadius\] {
  border-radius: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-consentBlock-purposes-list-items-cornerRadius\] {
  border-radius: var(--k-consentGate-consentBlock-purposes-list-items-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-container-cornerRadius\] {
  border-radius: var(--k-consentGate-container-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-consentGate-header-closeButton-cornerRadius\] {
  border-radius: var(--k-consentGate-header-closeButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-container-cornerRadius\] {
  border-radius: var(--k-modal-container-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-footer-actionButton-cornerRadius\] {
  border-radius: var(--k-modal-footer-actionButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-gpcBanner-cornerRadius\] {
  border-radius: var(--k-modal-gpcBanner-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-header-returnButton-cornerRadius\] {
  border-radius: var(--k-modal-header-returnButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-purposeList-purposeListItems-purposeCornerRadius\] {
  border-radius: var(--k-modal-purposeList-purposeListItems-purposeCornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-purposeListHeader-acceptAllButton-cornerRadius\] {
  border-radius: var(--k-modal-purposeListHeader-acceptAllButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-modal-purposeListHeader-rejectAllButton-cornerRadius\] {
  border-radius: var(--k-modal-purposeListHeader-rejectAllButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-exitButton-cornerRadius\] {
  border-radius: var(--k-preference-exitButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-navigation-layout-cornerRadius\] {
  border-radius: var(--k-preference-navigation-layout-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-navigation-layout-item-cornerRadius\] {
  border-radius: var(--k-preference-navigation-layout-item-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-purposes-footer-actionButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-purposes-footer-actionButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-purposes-gpcBanner-cornerRadius\] {
  border-radius: var(--k-preference-tabs-purposes-gpcBanner-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-purposes-purposeList-purposeListItems-purposeCornerRadius\] {
  border-radius: var(--k-preference-tabs-purposes-purposeList-purposeListItems-purposeCornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-home-dsrPortalLink-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-home-dsrPortalLink-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-home-rightsList-item-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-home-rightsList-item-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-rightForm-actionButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-rightForm-actionButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-rightForm-form-fields-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-rightForm-form-fields-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-rightForm-header-returnButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-rightForm-header-returnButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-submitted-footer-actionButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-submitted-footer-actionButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-requests-submitted-header-returnButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-requests-submitted-header-returnButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-subscriptions-footer-actionButton-cornerRadius\] {
  border-radius: var(--k-preference-tabs-subscriptions-footer-actionButton-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-subscriptions-list-layout-cornerRadius\] {
  border-radius: var(--k-preference-tabs-subscriptions-list-layout-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-\[--k-preference-tabs-subscriptions-unsubscribeAll-cornerRadius\] {
  border-radius: var(--k-preference-tabs-subscriptions-unsubscribeAll-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-none {
  border-radius: 0px !important;
}
#lanyard_root * .ketch-rounded-3xl {
  border-radius: 1.5rem;
}
#lanyard_root * .ketch-rounded-\[3px\] {
  border-radius: 3px;
}
#lanyard_root * .ketch-rounded-full {
  border-radius: 9999px;
}
#lanyard_root * .ketch-rounded-inherit {
  border-radius: inherit;
}
#lanyard_root * .ketch-rounded-none {
  border-radius: 0px;
}
#lanyard_root * .\!ketch-rounded-tl-\[--k-preference-navigation-layout-item-cornerRadius\] {
  border-top-left-radius: var(--k-preference-navigation-layout-item-cornerRadius) !important;
}
#lanyard_root * .\!ketch-rounded-tr-\[--k-preference-navigation-layout-item-cornerRadius\] {
  border-top-right-radius: var(--k-preference-navigation-layout-item-cornerRadius) !important;
}
#lanyard_root * .\!ketch-border-\[1px\] {
  border-width: 1px !important;
}
#lanyard_root * .ketch-border {
  border-width: 1px;
}
#lanyard_root * .ketch-border-0 {
  border-width: 0px;
}
#lanyard_root * .ketch-border-2 {
  border-width: 2px;
}
#lanyard_root * .ketch-border-\[1\.5px\] {
  border-width: 1.5px;
}
#lanyard_root * .ketch-border-x-0 {
  border-left-width: 0px;
  border-right-width: 0px;
}
#lanyard_root * .ketch-border-b {
  border-bottom-width: 1px;
}
#lanyard_root * .ketch-border-l-0 {
  border-left-width: 0px;
}
#lanyard_root * .ketch-border-r-0 {
  border-right-width: 0px;
}
#lanyard_root * .ketch-border-t-0 {
  border-top-width: 0px;
}
#lanyard_root * .\!ketch-border-solid {
  border-style: solid !important;
}
#lanyard_root * .ketch-border-solid {
  border-style: solid;
}
#lanyard_root * .ketch-border-none {
  border-style: none;
}
#lanyard_root * .\!ketch-border-\[--k-banner-buttons-primary-background-color\] {
  border-color: var(--k-banner-buttons-primary-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-banner-buttons-secondary-background-color\] {
  border-color: var(--k-banner-buttons-secondary-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-banner-buttons-tertiary-background-color\] {
  border-color: var(--k-banner-buttons-tertiary-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-banner-gpcBanner-outline-color\] {
  border-color: var(--k-banner-gpcBanner-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-actionBlock-button-outline-color\] {
  border-color: var(--k-consentGate-actionBlock-button-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-consentBlock-button-background-color\] {
  border-color: var(--k-consentGate-consentBlock-button-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-background-color\] {
  border-color: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-background-color\] {
  border-color: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-consentBlock-purposes-list-items-purposeOutline-color\] {
  border-color: var(--k-consentGate-consentBlock-purposes-list-items-purposeOutline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-consentBlock-purposes-list-switchButtons-off-background-color\] {
  border-color: var(--k-consentGate-consentBlock-purposes-list-switchButtons-off-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-consentGate-header-closeButton-icon-color\] {
  border-color: var(--k-consentGate-header-closeButton-icon-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-modal-footer-actionButton-background-color\] {
  border-color: var(--k-modal-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-modal-gpcBanner-outline-color\] {
  border-color: var(--k-modal-gpcBanner-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-modal-purposeList-purposeListItems-purposeOutline-color\] {
  border-color: var(--k-modal-purposeList-purposeListItems-purposeOutline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-modal-purposeList-switchButtons-off-background-color\] {
  border-color: var(--k-modal-purposeList-switchButtons-off-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-modal-purposeListHeader-acceptAllButton-background-color\] {
  border-color: var(--k-modal-purposeListHeader-acceptAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-modal-purposeListHeader-rejectAllButton-background-color\] {
  border-color: var(--k-modal-purposeListHeader-rejectAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-purposes-footer-actionButton-background-color\] {
  border-color: var(--k-preference-tabs-purposes-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-purposes-gpcBanner-outline-color\] {
  border-color: var(--k-preference-tabs-purposes-gpcBanner-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-purposes-purposeList-purposeListItems-purposeOutline-color\] {
  border-color: var(--k-preference-tabs-purposes-purposeList-purposeListItems-purposeOutline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-purposes-purposeList-switchButtons-off-background-color\] {
  border-color: var(--k-preference-tabs-purposes-purposeList-switchButtons-off-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-background-color\] {
  border-color: var(--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-background-color\] {
  border-color: var(--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-requests-rightForm-actionButton-background-color\] {
  border-color: var(--k-preference-tabs-requests-rightForm-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-requests-rightForm-form-checkboxes-error-background-color\] {
  border-color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-error-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-requests-rightForm-form-checkboxes-unselected-background-color\] {
  border-color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-unselected-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-requests-rightForm-form-fields-error-outline-color\] {
  border-color: var(--k-preference-tabs-requests-rightForm-form-fields-error-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-requests-rightForm-form-fields-inactive-outline-color\] {
  border-color: var(--k-preference-tabs-requests-rightForm-form-fields-inactive-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-requests-submitted-footer-actionButton-outline-color\] {
  border-color: var(--k-preference-tabs-requests-submitted-footer-actionButton-outline-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-subscriptions-footer-actionButton-background-color\] {
  border-color: var(--k-preference-tabs-subscriptions-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-subscriptions-list-checkbox-unselected-background-color\] {
  border-color: var(--k-preference-tabs-subscriptions-list-checkbox-unselected-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-preference-tabs-subscriptions-list-layout-background-color\] {
  border-color: var(--k-preference-tabs-subscriptions-list-layout-background-color) !important;
}
#lanyard_root * .\!ketch-border-\[--k-tabs-subscriptions-list-checkbox-error-text-color\] {
  border-color: var(--k-tabs-subscriptions-list-checkbox-error-text-color) !important;
}
#lanyard_root * .ketch-border-black {
  --tw-border-opacity: 1;
  border-color: rgb(0 0 0 / var(--tw-border-opacity));
}
#lanyard_root * .ketch-border-gray-300 {
  --tw-border-opacity: 1;
  border-color: rgb(209 213 219 / var(--tw-border-opacity));
}
#lanyard_root * .ketch-border-gray-400 {
  --tw-border-opacity: 1;
  border-color: rgb(156 163 175 / var(--tw-border-opacity));
}
#lanyard_root * .ketch-border-ketch-error {
  border-color: rgba(252, 60, 96, 1);
}
#lanyard_root * .\!ketch-bg-\[--k-banner-buttons-primary-background-color\] {
  background-color: var(--k-banner-buttons-primary-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-banner-buttons-secondary-background-color\] {
  background-color: var(--k-banner-buttons-secondary-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-banner-buttons-tertiary-background-color\] {
  background-color: var(--k-banner-buttons-tertiary-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-banner-container-backdrop-background-color\] {
  background-color: var(--k-banner-container-backdrop-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-banner-container-background-color\] {
  background-color: var(--k-banner-container-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-banner-gpcBanner-fill-color\] {
  background-color: var(--k-banner-gpcBanner-fill-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-banner-header-returnButton-background-color\] {
  background-color: var(--k-banner-header-returnButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-actionBlock-button-background-color\] {
  background-color: var(--k-consentGate-actionBlock-button-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-consentBlock-button-background-color\] {
  background-color: var(--k-consentGate-consentBlock-button-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-background-color\] {
  background-color: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-background-color\] {
  background-color: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-consentBlock-purposes-list-items-purposeFill-color\] {
  background-color: var(--k-consentGate-consentBlock-purposes-list-items-purposeFill-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-consentBlock-purposes-list-switchButtons-off-background-color\] {
  background-color: var(--k-consentGate-consentBlock-purposes-list-switchButtons-off-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-container-background-color\] {
  background-color: var(--k-consentGate-container-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-header-background\] {
  background-color: var(--k-consentGate-header-background) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-consentGate-header-closeButton-background-color\] {
  background-color: var(--k-consentGate-header-closeButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-container-backdrop-background-color\] {
  background-color: var(--k-modal-container-backdrop-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-container-background-color\] {
  background-color: var(--k-modal-container-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-footer-actionButton-background-color\] {
  background-color: var(--k-modal-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-footer-background-color\] {
  background-color: var(--k-modal-footer-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-gpcBanner-fill-color\] {
  background-color: var(--k-modal-gpcBanner-fill-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-header-background-color\] {
  background-color: var(--k-modal-header-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-header-returnButton-background-color\] {
  background-color: var(--k-modal-header-returnButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-purposeList-purposeListItems-purposeFill-color\] {
  background-color: var(--k-modal-purposeList-purposeListItems-purposeFill-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-purposeList-switchButtons-off-background-color\] {
  background-color: var(--k-modal-purposeList-switchButtons-off-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-purposeListHeader-acceptAllButton-background-color\] {
  background-color: var(--k-modal-purposeListHeader-acceptAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-modal-purposeListHeader-rejectAllButton-background-color\] {
  background-color: var(--k-modal-purposeListHeader-rejectAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-container-background-color\] {
  background-color: var(--k-preference-container-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-exitButton-background-color\] {
  background-color: var(--k-preference-exitButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-header-background-color\] {
  background-color: var(--k-preference-header-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-navigation-layout-background-color\] {
  background-color: var(--k-preference-navigation-layout-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-navigation-layout-item-selectedBackground-color\] {
  background-color: var(--k-preference-navigation-layout-item-selectedBackground-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-navigation-layout-item-unselectedBackground-color\] {
  background-color: var(--k-preference-navigation-layout-item-unselectedBackground-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-footer-actionButton-background-color\] {
  background-color: var(--k-preference-tabs-purposes-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-footer-background-color\] {
  background-color: var(--k-preference-tabs-purposes-footer-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-gpcBanner-fill-color\] {
  background-color: var(--k-preference-tabs-purposes-gpcBanner-fill-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-purposeList-purposeListItems-purposeFill-color\] {
  background-color: var(--k-preference-tabs-purposes-purposeList-purposeListItems-purposeFill-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-purposeList-switchButtons-off-background-color\] {
  background-color: var(--k-preference-tabs-purposes-purposeList-switchButtons-off-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-background-color\] {
  background-color: var(--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-background-color\] {
  background-color: var(--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-home-dsrPortalLink-background-color\] {
  background-color: var(--k-preference-tabs-requests-home-dsrPortalLink-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-home-rightsList-item-background-color\] {
  background-color: var(--k-preference-tabs-requests-home-rightsList-item-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-rightForm-actionButton-background-color\] {
  background-color: var(--k-preference-tabs-requests-rightForm-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-rightForm-form-checkboxes-unselected-background-color\] {
  background-color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-unselected-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-rightForm-form-fields-error-background-color\] {
  background-color: var(--k-preference-tabs-requests-rightForm-form-fields-error-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-rightForm-form-fields-inactive-background-color\] {
  background-color: var(--k-preference-tabs-requests-rightForm-form-fields-inactive-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-rightForm-header-returnButton-background-color\] {
  background-color: var(--k-preference-tabs-requests-rightForm-header-returnButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-submitted-footer-actionButton-background-color\] {
  background-color: var(--k-preference-tabs-requests-submitted-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-submitted-footer-background-color\] {
  background-color: var(--k-preference-tabs-requests-submitted-footer-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-requests-submitted-header-returnButton-background-color\] {
  background-color: var(--k-preference-tabs-requests-submitted-header-returnButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-footer-actionButton-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-footer-actionButton-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-footer-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-footer-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-list-checkbox-unselected-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-list-checkbox-unselected-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-list-layout-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-list-layout-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-list-switchButton-off-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-list-switchButton-off-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-unsubscribeAll-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-unsubscribeAll-background-color) !important;
}
#lanyard_root * .\!ketch-bg-\[--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-off-background-color\] {
  background-color: var(--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-off-background-color) !important;
}
#lanyard_root * .ketch-bg-gray-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(229 231 235 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-gray-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(209 213 219 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-gray-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(107 114 128 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-inherit {
  background-color: inherit;
}
#lanyard_root * .ketch-bg-ketch-black-black-10 {
  background-color: rgba(7, 26, 36, 0.1);
}
#lanyard_root * .ketch-bg-ketch-black-black-100 {
  background-color: rgba(7, 26, 36, 1);
}
#lanyard_root * .ketch-bg-ketch-white-24 {
  background-color: rgba(255, 255, 255, 0.24);
}
#lanyard_root * .ketch-bg-orange-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 215 170 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-orange-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(251 146 60 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-orange-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(234 88 12 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-slate-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(226 232 240 / var(--tw-bg-opacity));
}
#lanyard_root * .ketch-bg-transparent {
  background-color: transparent;
}
#lanyard_root * .ketch-bg-white {
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}
#lanyard_root * .\!ketch-fill-\[--k-banner-header-returnButton-icon-color\] {
  fill: var(--k-banner-header-returnButton-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-consentGate-actionBlock-button-icon-color\] {
  fill: var(--k-consentGate-actionBlock-button-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-consentGate-consentBlock-purposes-list-items-arrowIcon-color\] {
  fill: var(--k-consentGate-consentBlock-purposes-list-items-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-consentGate-consentBlock-purposes-list-items-purposeLinks-color\] {
  fill: var(--k-consentGate-consentBlock-purposes-list-items-purposeLinks-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-consentGate-header-closeButton-icon-color\] {
  fill: var(--k-consentGate-header-closeButton-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-modal-header-returnButton-icon-color\] {
  fill: var(--k-modal-header-returnButton-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-modal-purposeList-purposeListItems-arrowIcon-color\] {
  fill: var(--k-modal-purposeList-purposeListItems-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-modal-purposeList-purposeListItems-purposeLinks-color\] {
  fill: var(--k-modal-purposeList-purposeListItems-purposeLinks-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-modal-purposeListHeader-title-color\] {
  fill: var(--k-modal-purposeListHeader-title-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-exitButton-iconColor-color\] {
  fill: var(--k-preference-exitButton-iconColor-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-navigation-layout-item-arrowIcon-color\] {
  fill: var(--k-preference-navigation-layout-item-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-purposes-purposeList-purposeListItems-arrowIcon-color\] {
  fill: var(--k-preference-tabs-purposes-purposeList-purposeListItems-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-purposes-purposeList-purposeListItems-purposeLinks-color\] {
  fill: var(--k-preference-tabs-purposes-purposeList-purposeListItems-purposeLinks-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-purposes-purposeListHeader-title-color\] {
  fill: var(--k-preference-tabs-purposes-purposeListHeader-title-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-requests-form-dropdown-arrow-icon-color\] {
  fill: var(--k-preference-tabs-requests-form-dropdown-arrow-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-requests-home-dsrPortalLink-arrowIcon-color\] {
  fill: var(--k-preference-tabs-requests-home-dsrPortalLink-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-requests-home-rightsList-item-arrowIcon-color\] {
  fill: var(--k-preference-tabs-requests-home-rightsList-item-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-requests-rightForm-header-returnButton-icon-color\] {
  fill: var(--k-preference-tabs-requests-rightForm-header-returnButton-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-requests-submitted-footer-actionButton-icon-color\] {
  fill: var(--k-preference-tabs-requests-submitted-footer-actionButton-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-requests-submitted-header-returnButton-icon-color\] {
  fill: var(--k-preference-tabs-requests-submitted-header-returnButton-icon-color) !important;
}
#lanyard_root * .\!ketch-fill-\[--k-preference-tabs-welcome-quickLinks-link-color\] {
  fill: var(--k-preference-tabs-welcome-quickLinks-link-color) !important;
}
#lanyard_root * .ketch-fill-\[--k-consentGate-actionBlock-footer-link-text-color\] {
  fill: var(--k-consentGate-actionBlock-footer-link-text-color);
}
#lanyard_root * .ketch-fill-\[--k-preference-tabs-requests-form-error-text-color\] {
  fill: var(--k-preference-tabs-requests-form-error-text-color);
}
#lanyard_root * .ketch-fill-\[--k-preference-welcome-quickLinks-link-color\] {
  fill: var(--k-preference-welcome-quickLinks-link-color);
}
#lanyard_root * .ketch-fill-black {
  fill: #000;
}
#lanyard_root * .ketch-fill-inherit {
  fill: inherit;
}
#lanyard_root * .ketch-fill-ketch-black-black-100 {
  fill: rgba(7, 26, 36, 1);
}
#lanyard_root * .ketch-fill-white {
  fill: #fff;
}
#lanyard_root * .\!ketch-stroke-\[--k-preference-tabs-requests-form-dropdown-arrow-icon-color\] {
  stroke: var(--k-preference-tabs-requests-form-dropdown-arrow-icon-color) !important;
}
#lanyard_root * .ketch-stroke-\[--k-preference-tabs-requests-form-error-text-color\] {
  stroke: var(--k-preference-tabs-requests-form-error-text-color);
}
#lanyard_root * .ketch-stroke-black {
  stroke: #000;
}
#lanyard_root * .ketch-stroke-current {
  stroke: currentColor;
}
#lanyard_root * .ketch-stroke-white {
  stroke: #fff;
}
#lanyard_root * .ketch-object-contain {
  -o-object-fit: contain;
     object-fit: contain;
}
#lanyard_root * .\!ketch-p-0 {
  padding: 0 !important;
}
#lanyard_root * .\!ketch-p-4 {
  padding: 16px !important;
}
#lanyard_root * .ketch-p-0 {
  padding: 0;
}
#lanyard_root * .ketch-p-2 {
  padding: 8px;
}
#lanyard_root * .ketch-p-3 {
  padding: 12px;
}
#lanyard_root * .ketch-p-4 {
  padding: 16px;
}
#lanyard_root * .ketch-px-0 {
  padding-left: 0;
  padding-right: 0;
}
#lanyard_root * .ketch-px-1 {
  padding-left: 4px;
  padding-right: 4px;
}
#lanyard_root * .ketch-px-1\.5 {
  padding-left: 6px;
  padding-right: 6px;
}
#lanyard_root * .ketch-px-2 {
  padding-left: 8px;
  padding-right: 8px;
}
#lanyard_root * .ketch-px-3 {
  padding-left: 12px;
  padding-right: 12px;
}
#lanyard_root * .ketch-px-4 {
  padding-left: 16px;
  padding-right: 16px;
}
#lanyard_root * .ketch-px-5 {
  padding-left: 20px;
  padding-right: 20px;
}
#lanyard_root * .ketch-px-6 {
  padding-left: 24px;
  padding-right: 24px;
}
#lanyard_root * .ketch-px-8 {
  padding-left: 32px;
  padding-right: 32px;
}
#lanyard_root * .ketch-px-\[1px\] {
  padding-left: 1px;
  padding-right: 1px;
}
#lanyard_root * .ketch-py-0 {
  padding-top: 0;
  padding-bottom: 0;
}
#lanyard_root * .ketch-py-0\.5 {
  padding-top: 2px;
  padding-bottom: 2px;
}
#lanyard_root * .ketch-py-1 {
  padding-top: 4px;
  padding-bottom: 4px;
}
#lanyard_root * .ketch-py-2 {
  padding-top: 8px;
  padding-bottom: 8px;
}
#lanyard_root * .ketch-py-20 {
  padding-top: 80px;
  padding-bottom: 80px;
}
#lanyard_root * .ketch-py-3 {
  padding-top: 12px;
  padding-bottom: 12px;
}
#lanyard_root * .ketch-py-4 {
  padding-top: 16px;
  padding-bottom: 16px;
}
#lanyard_root * .ketch-py-5 {
  padding-top: 20px;
  padding-bottom: 20px;
}
#lanyard_root * .ketch-py-6 {
  padding-top: 24px;
  padding-bottom: 24px;
}
#lanyard_root * .ketch-py-\[1px\] {
  padding-top: 1px;
  padding-bottom: 1px;
}
#lanyard_root * .ketch-pb-0 {
  padding-bottom: 0;
}
#lanyard_root * .ketch-pb-1 {
  padding-bottom: 4px;
}
#lanyard_root * .ketch-pb-2 {
  padding-bottom: 8px;
}
#lanyard_root * .ketch-pb-3 {
  padding-bottom: 12px;
}
#lanyard_root * .ketch-pb-4 {
  padding-bottom: 16px;
}
#lanyard_root * .ketch-pb-6 {
  padding-bottom: 24px;
}
#lanyard_root * .ketch-pb-8 {
  padding-bottom: 32px;
}
#lanyard_root * .ketch-pb-\[--safe-area-inset-bottom\] {
  padding-bottom: var(--safe-area-inset-bottom);
}
#lanyard_root * .ketch-pb-\[max\(16px\,var\(--safe-area-inset-bottom\)\)\] {
  padding-bottom: max(16px,var(--safe-area-inset-bottom));
}
#lanyard_root * .ketch-pl-0 {
  padding-left: 0;
}
#lanyard_root * .ketch-pl-1 {
  padding-left: 4px;
}
#lanyard_root * .ketch-pl-10 {
  padding-left: 40px;
}
#lanyard_root * .ketch-pl-2 {
  padding-left: 8px;
}
#lanyard_root * .ketch-pl-3 {
  padding-left: 12px;
}
#lanyard_root * .ketch-pl-4 {
  padding-left: 16px;
}
#lanyard_root * .ketch-pl-5 {
  padding-left: 20px;
}
#lanyard_root * .ketch-pl-6 {
  padding-left: 24px;
}
#lanyard_root * .ketch-pl-\[--safe-area-inset-left\] {
  padding-left: var(--safe-area-inset-left);
}
#lanyard_root * .ketch-pl-\[calc\(16px\+var\(--safe-area-inset-left\)\)\] {
  padding-left: calc(16px + var(--safe-area-inset-left));
}
#lanyard_root * .ketch-pl-\[calc\(var\(--safe-area-inset-left\)\+4px\)\] {
  padding-left: calc(var(--safe-area-inset-left) + 4px);
}
#lanyard_root * .ketch-pl-\[max\(16px\,var\(--safe-area-inset-left\)\)\] {
  padding-left: max(16px,var(--safe-area-inset-left));
}
#lanyard_root * .ketch-pr-0 {
  padding-right: 0;
}
#lanyard_root * .ketch-pr-14 {
  padding-right: 56px;
}
#lanyard_root * .ketch-pr-3 {
  padding-right: 12px;
}
#lanyard_root * .ketch-pr-6 {
  padding-right: 24px;
}
#lanyard_root * .ketch-pr-8 {
  padding-right: 32px;
}
#lanyard_root * .ketch-pr-\[--safe-area-inset-right\] {
  padding-right: var(--safe-area-inset-right);
}
#lanyard_root * .ketch-pr-\[calc\(16px\+var\(--safe-area-inset-right\)\)\] {
  padding-right: calc(16px + var(--safe-area-inset-right));
}
#lanyard_root * .ketch-pr-\[calc\(var\(--safe-area-inset-right\)\+4px\)\] {
  padding-right: calc(var(--safe-area-inset-right) + 4px);
}
#lanyard_root * .ketch-pr-\[max\(16px\,var\(--safe-area-inset-right\)\)\] {
  padding-right: max(16px,var(--safe-area-inset-right));
}
#lanyard_root * .ketch-pt-0\.5 {
  padding-top: 2px;
}
#lanyard_root * .ketch-pt-1 {
  padding-top: 4px;
}
#lanyard_root * .ketch-pt-2 {
  padding-top: 8px;
}
#lanyard_root * .ketch-pt-3 {
  padding-top: 12px;
}
#lanyard_root * .ketch-pt-4 {
  padding-top: 16px;
}
#lanyard_root * .ketch-pt-5 {
  padding-top: 20px;
}
#lanyard_root * .ketch-pt-8 {
  padding-top: 32px;
}
#lanyard_root * .ketch-pt-\[--safe-area-inset-top\] {
  padding-top: var(--safe-area-inset-top);
}
#lanyard_root * .ketch-pt-\[max\(16px\,var\(--safe-area-inset-top\)\)\] {
  padding-top: max(16px,var(--safe-area-inset-top));
}
#lanyard_root * .ketch-text-left {
  text-align: left;
}
#lanyard_root * .ketch-text-center {
  text-align: center;
}
#lanyard_root * .\!ketch-text-ketch-h2 {
  font-size: 20px !important;
  line-height: 30px !important;
}
#lanyard_root * .\!ketch-text-ketch-l {
  font-size: 14px !important;
  line-height: 21px !important;
}
#lanyard_root * .ketch-text-ketch-h0 {
  font-size: 32px;
  line-height: 48px;
}
#lanyard_root * .ketch-text-ketch-h1 {
  font-size: 28px;
  line-height: 39px;
}
#lanyard_root * .ketch-text-ketch-h1-small {
  font-size: 26px;
  line-height: 36.4px;
}
#lanyard_root * .ketch-text-ketch-h2 {
  font-size: 20px;
  line-height: 30px;
}
#lanyard_root * .ketch-text-ketch-h3 {
  font-size: 18px;
  line-height: 22.5px;
}
#lanyard_root * .ketch-text-ketch-h4 {
  font-size: 16px;
  line-height: 24px;
}
#lanyard_root * .ketch-text-ketch-l {
  font-size: 14px;
  line-height: 21px;
}
#lanyard_root * .ketch-text-ketch-lm {
  font-size: 14px;
  line-height: 21px;
}
#lanyard_root * .ketch-text-ketch-m {
  font-size: 13px;
  line-height: 16px;
}
#lanyard_root * .ketch-text-ketch-s {
  font-size: 12px;
  line-height: 15px;
}
#lanyard_root * .ketch-text-ketch-xs {
  font-size: 10px;
  line-height: 14.5px;
  font-weight: 500;
}
#lanyard_root * .\!ketch-font-\[--k-banner-container-font\] {
  font-weight: var(--k-banner-container-font) !important;
}
#lanyard_root * .\!ketch-font-\[--k-modal-container-font\] {
  font-weight: var(--k-modal-container-font) !important;
}
#lanyard_root * .ketch-font-bold {
  font-weight: 700;
}
#lanyard_root * .ketch-font-medium {
  font-weight: 500;
}
#lanyard_root * .ketch-font-normal {
  font-weight: 400;
}
#lanyard_root * .ketch-font-semibold {
  font-weight: 600;
}
#lanyard_root * .ketch-font-weight-inherit {
  font-weight: inherit;
}
#lanyard_root * .ketch-uppercase {
  text-transform: uppercase;
}
#lanyard_root * .ketch-italic {
  font-style: italic;
}
#lanyard_root * .ketch-leading-3 {
  line-height: .75rem;
}
#lanyard_root * .ketch-leading-4 {
  line-height: 1rem;
}
#lanyard_root * .ketch-tracking-\[-0\.12px\] {
  letter-spacing: -0.12px;
}
#lanyard_root * .ketch-tracking-\[-0\.13px\] {
  letter-spacing: -0.13px;
}
#lanyard_root * .ketch-tracking-\[-0\.14px\] {
  letter-spacing: -0.14px;
}
#lanyard_root * .ketch-tracking-\[-0\.16px\] {
  letter-spacing: -0.16px;
}
#lanyard_root * .ketch-tracking-\[-0\.18px\] {
  letter-spacing: -0.18px;
}
#lanyard_root * .ketch-tracking-\[-0\.1px\] {
  letter-spacing: -0.1px;
}
#lanyard_root * .ketch-tracking-\[-0\.26px\] {
  letter-spacing: -0.26px;
}
#lanyard_root * .ketch-tracking-\[-0\.28px\] {
  letter-spacing: -0.28px;
}
#lanyard_root * .ketch-tracking-\[-0\.2px\] {
  letter-spacing: -0.2px;
}
#lanyard_root * .ketch-tracking-\[-0\.64px\] {
  letter-spacing: -0.64px;
}
#lanyard_root * .\!ketch-text-\[--k-banner-buttons-primary-text-color\] {
  color: var(--k-banner-buttons-primary-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-buttons-secondary-text-color\] {
  color: var(--k-banner-buttons-secondary-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-buttons-tertiary-text-color\] {
  color: var(--k-banner-buttons-tertiary-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-description-link-color\] {
  color: var(--k-banner-description-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-description-text-color\] {
  color: var(--k-banner-description-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-gpcBanner-description-text-color\] {
  color: var(--k-banner-gpcBanner-description-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-gpcBanner-title-text-color\] {
  color: var(--k-banner-gpcBanner-title-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-header-returnButton-text-color\] {
  color: var(--k-banner-header-returnButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-banner-header-title-color\] {
  color: var(--k-banner-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-actionBlock-button-text-color\] {
  color: var(--k-consentGate-actionBlock-button-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-actionBlock-footer-link-text-color\] {
  color: var(--k-consentGate-actionBlock-footer-link-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-actionBlock-footer-teaser-text-color\] {
  color: var(--k-consentGate-actionBlock-footer-teaser-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-actionBlock-header-description-color\] {
  color: var(--k-consentGate-actionBlock-header-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-actionBlock-header-description-link-color\] {
  color: var(--k-consentGate-actionBlock-header-description-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-actionBlock-header-title-color\] {
  color: var(--k-consentGate-actionBlock-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-button-text-color\] {
  color: var(--k-consentGate-consentBlock-button-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-footer-links-color\] {
  color: var(--k-consentGate-consentBlock-footer-links-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-header-description-color\] {
  color: var(--k-consentGate-consentBlock-header-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-header-description-link-color\] {
  color: var(--k-consentGate-consentBlock-header-description-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-header-title-color\] {
  color: var(--k-consentGate-consentBlock-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-text-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-acceptAllButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-text-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-bulkActionButtons-rejectAllButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-header-title-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-items-arrowIcon-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-items-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-items-purposeContent-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-items-purposeContent-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-items-purposeLinks-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-items-purposeLinks-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-switchButtons-off-text-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-switchButtons-off-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-consentBlock-purposes-list-switchButtons-on-text-color\] {
  color: var(--k-consentGate-consentBlock-purposes-list-switchButtons-on-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-header-closeButton-text-color\] {
  color: var(--k-consentGate-header-closeButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-consentGate-header-title-color\] {
  color: var(--k-consentGate-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-description-link-color\] {
  color: var(--k-modal-description-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-description-text-color\] {
  color: var(--k-modal-description-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-description-title-color\] {
  color: var(--k-modal-description-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-footer-actionButton-text-color\] {
  color: var(--k-modal-footer-actionButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-gpcBanner-description-text-color\] {
  color: var(--k-modal-gpcBanner-description-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-gpcBanner-title-text-color\] {
  color: var(--k-modal-gpcBanner-title-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-header-returnButton-text-color\] {
  color: var(--k-modal-header-returnButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-header-title-color\] {
  color: var(--k-modal-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeList-purposeListItems-arrowIcon-color\] {
  color: var(--k-modal-purposeList-purposeListItems-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeList-purposeListItems-purposeContent-color\] {
  color: var(--k-modal-purposeList-purposeListItems-purposeContent-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeList-purposeListItems-purposeLinks-color\] {
  color: var(--k-modal-purposeList-purposeListItems-purposeLinks-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeList-switchButtons-off-text-color\] {
  color: var(--k-modal-purposeList-switchButtons-off-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeList-switchButtons-on-text-color\] {
  color: var(--k-modal-purposeList-switchButtons-on-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeListHeader-acceptAllButton-text-color\] {
  color: var(--k-modal-purposeListHeader-acceptAllButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeListHeader-rejectAllButton-text-color\] {
  color: var(--k-modal-purposeListHeader-rejectAllButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-modal-purposeListHeader-title-color\] {
  color: var(--k-modal-purposeListHeader-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-exitButton-text-color\] {
  color: var(--k-preference-exitButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-header-title-color\] {
  color: var(--k-preference-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-navigation-layout-item-selectedText-color\] {
  color: var(--k-preference-navigation-layout-item-selectedText-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-navigation-layout-item-unselectedText-color\] {
  color: var(--k-preference-navigation-layout-item-unselectedText-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-footer-actionButton-text-color\] {
  color: var(--k-preference-tabs-purposes-footer-actionButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-gpcBanner-description-text-color\] {
  color: var(--k-preference-tabs-purposes-gpcBanner-description-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-gpcBanner-title-text-color\] {
  color: var(--k-preference-tabs-purposes-gpcBanner-title-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-header-description-color\] {
  color: var(--k-preference-tabs-purposes-header-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-header-link-color\] {
  color: var(--k-preference-tabs-purposes-header-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-header-title-color\] {
  color: var(--k-preference-tabs-purposes-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeList-purposeListItems-arrowIcon-color\] {
  color: var(--k-preference-tabs-purposes-purposeList-purposeListItems-arrowIcon-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeList-purposeListItems-purposeContent-color\] {
  color: var(--k-preference-tabs-purposes-purposeList-purposeListItems-purposeContent-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeList-purposeListItems-purposeLinks-color\] {
  color: var(--k-preference-tabs-purposes-purposeList-purposeListItems-purposeLinks-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeList-switchButtons-off-text-color\] {
  color: var(--k-preference-tabs-purposes-purposeList-switchButtons-off-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeList-switchButtons-on-text-color\] {
  color: var(--k-preference-tabs-purposes-purposeList-switchButtons-on-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-text-color\] {
  color: var(--k-preference-tabs-purposes-purposeListHeader-acceptAllButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-text-color\] {
  color: var(--k-preference-tabs-purposes-purposeListHeader-rejectAllButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-purposes-purposeListHeader-title-color\] {
  color: var(--k-preference-tabs-purposes-purposeListHeader-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-form-error-text-color\] {
  color: var(--k-preference-tabs-requests-form-error-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-dsrPortalLink-description-color\] {
  color: var(--k-preference-tabs-requests-home-dsrPortalLink-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-dsrPortalLink-title-color\] {
  color: var(--k-preference-tabs-requests-home-dsrPortalLink-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-header-description-color\] {
  color: var(--k-preference-tabs-requests-home-header-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-header-link-color\] {
  color: var(--k-preference-tabs-requests-home-header-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-header-title-color\] {
  color: var(--k-preference-tabs-requests-home-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-rightsList-item-title-color\] {
  color: var(--k-preference-tabs-requests-home-rightsList-item-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-home-rightsList-title-color\] {
  color: var(--k-preference-tabs-requests-home-rightsList-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-actionButton-text-color\] {
  color: var(--k-preference-tabs-requests-rightForm-actionButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-checkboxes-error-label-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-error-label-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-checkboxes-selected-label-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-selected-label-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-checkboxes-unselected-label-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-unselected-label-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-dividers-subtitle-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-dividers-subtitle-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-dividers-title-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-dividers-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-fields-fieldLabel-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-fields-fieldLabel-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-fields-hintText-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-fields-hintText-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-fields-inputText-color\] {
  color: var(--k-preference-tabs-requests-rightForm-form-fields-inputText-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-rightForm-header-title-color\] {
  color: var(--k-preference-tabs-requests-rightForm-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-submitted-footer-actionButton-text-color\] {
  color: var(--k-preference-tabs-requests-submitted-footer-actionButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-submitted-header-title-color\] {
  color: var(--k-preference-tabs-requests-submitted-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-submitted-text-description-color\] {
  color: var(--k-preference-tabs-requests-submitted-text-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-requests-submitted-text-title-color\] {
  color: var(--k-preference-tabs-requests-submitted-text-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-footer-actionButton-text-color\] {
  color: var(--k-preference-tabs-subscriptions-footer-actionButton-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-header-description-color\] {
  color: var(--k-preference-tabs-subscriptions-header-description-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-header-link-color\] {
  color: var(--k-preference-tabs-subscriptions-header-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-header-title-color\] {
  color: var(--k-preference-tabs-subscriptions-header-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-checkbox-selected-label-color\] {
  color: var(--k-preference-tabs-subscriptions-list-checkbox-selected-label-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-checkbox-text-color\] {
  color: var(--k-preference-tabs-subscriptions-list-checkbox-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-checkbox-unselected-label-color\] {
  color: var(--k-preference-tabs-subscriptions-list-checkbox-unselected-label-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-layout-link-color\] {
  color: var(--k-preference-tabs-subscriptions-list-layout-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-layout-text-color\] {
  color: var(--k-preference-tabs-subscriptions-list-layout-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-switchButton-off-text-color\] {
  color: var(--k-preference-tabs-subscriptions-list-switchButton-off-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-list-switchButton-on-text-color\] {
  color: var(--k-preference-tabs-subscriptions-list-switchButton-on-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-off-text-color\] {
  color: var(--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-off-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-on-text-color\] {
  color: var(--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-on-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-subscriptions-unsubscribeAll-text-color\] {
  color: var(--k-preference-tabs-subscriptions-unsubscribeAll-text-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-about-link-color\] {
  color: var(--k-preference-tabs-welcome-about-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-about-title-color\] {
  color: var(--k-preference-tabs-welcome-about-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-quickLinks-link-color\] {
  color: var(--k-preference-tabs-welcome-quickLinks-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-quickLinks-title-color\] {
  color: var(--k-preference-tabs-welcome-quickLinks-title-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-welcomeMsg-link-color\] {
  color: var(--k-preference-tabs-welcome-welcomeMsg-link-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-welcomeMsg-subtitle-color\] {
  color: var(--k-preference-tabs-welcome-welcomeMsg-subtitle-color) !important;
}
#lanyard_root * .\!ketch-text-\[--k-preference-tabs-welcome-welcomeMsg-title-color\] {
  color: var(--k-preference-tabs-welcome-welcomeMsg-title-color) !important;
}
#lanyard_root * .ketch-text-\[--k-preference-tabs-welcome-about-text-color\] {
  color: var(--k-preference-tabs-welcome-about-text-color);
}
#lanyard_root * .ketch-text-black {
  --tw-text-opacity: 1;
  color: rgb(0 0 0 / var(--tw-text-opacity));
}
#lanyard_root * .ketch-text-gray-700 {
  --tw-text-opacity: 1;
  color: rgb(55 65 81 / var(--tw-text-opacity));
}
#lanyard_root * .ketch-text-gray-900 {
  --tw-text-opacity: 1;
  color: rgb(17 24 39 / var(--tw-text-opacity));
}
#lanyard_root * .ketch-text-inherit {
  color: inherit;
}
#lanyard_root * .ketch-text-ketch-black-black-100 {
  color: rgba(7, 26, 36, 1);
}
#lanyard_root * .ketch-text-ketch-black-black-48 {
  color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * .ketch-text-ketch-black-black-56 {
  color: rgba(7, 26, 36, 0.56);
}
#lanyard_root * .ketch-text-ketch-error {
  color: rgba(252, 60, 96, 1);
}
#lanyard_root * .ketch-text-white {
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}
#lanyard_root * .\!ketch-underline {
  text-decoration-line: underline !important;
}
#lanyard_root * .ketch-underline {
  text-decoration-line: underline;
}
#lanyard_root * .ketch-no-underline {
  text-decoration-line: none;
}
#lanyard_root * .ketch-placeholder-ketch-black-black-48::-moz-placeholder {
  color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * .ketch-placeholder-ketch-black-black-48::placeholder {
  color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * .ketch-opacity-0 {
  opacity: 0;
}
#lanyard_root * .ketch-opacity-100 {
  opacity: 1;
}
#lanyard_root * .ketch-opacity-50 {
  opacity: 0.5;
}
#lanyard_root * .ketch-opacity-\[\.24\] {
  opacity: .24;
}
#lanyard_root * .ketch-opacity-\[0\.48\] {
  opacity: 0.48;
}
#lanyard_root * .ketch-opacity-\[0\.65\] {
  opacity: 0.65;
}
#lanyard_root * .ketch-shadow-\[0px_3px_10px_1px_rgba\(7\,26\,36\,0\.24\)\] {
  --tw-shadow: 0px 3px 10px 1px rgba(7,26,36,0.24);
  --tw-shadow-colored: 0px 3px 10px 1px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
#lanyard_root * .ketch-shadow-md {
  --tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
#lanyard_root * .ketch-shadow-none {
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
#lanyard_root * .ketch-outline-none {
  outline: 2px solid transparent;
  outline-offset: 2px;
}
#lanyard_root * .\!ketch-outline-2 {
  outline-width: 2px !important;
}
#lanyard_root * .\!ketch-outline-offset-2 {
  outline-offset: 2px !important;
}
#lanyard_root * .\!ketch-outline-ketch-black-black-100 {
  outline-color: rgba(7, 26, 36, 1) !important;
}
#lanyard_root * .\!ketch-outline-white {
  outline-color: #fff !important;
}
#lanyard_root * .ketch-outline-default-outline {
  outline-color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * .ketch-transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#lanyard_root * .ketch-transition-opacity {
  transition-property: opacity;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#lanyard_root * .ketch-transition-transform {
  transition-property: transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
#lanyard_root * .ketch-duration-1000 {
  transition-duration: 1000ms;
}
#lanyard_root * .ketch-duration-300 {
  transition-duration: 300ms;
}
#lanyard_root * .ketch-ease-in-out {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}
@supports (padding: max(0px)) {
  .banner-mobile-bottom {
    bottom: 0px !important;
  }

  /* CSS Collision where text is uppercase */
  #lanyard_root * {
    text-transform: none;
  }
}
#lanyard_root * .placeholder\:ketch-text-ketch-l::-moz-placeholder {
  font-size: 14px;
  line-height: 21px;
}
#lanyard_root * .placeholder\:ketch-text-ketch-l::placeholder {
  font-size: 14px;
  line-height: 21px;
}
#lanyard_root * .placeholder\:\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-fields-hintText-color\]::-moz-placeholder {
  color: var(--k-preference-tabs-requests-rightForm-form-fields-hintText-color) !important;
}
#lanyard_root * .placeholder\:\!ketch-text-\[--k-preference-tabs-requests-rightForm-form-fields-hintText-color\]::placeholder {
  color: var(--k-preference-tabs-requests-rightForm-form-fields-hintText-color) !important;
}
#lanyard_root * .before\:ketch-absolute::before {
  content: var(--tw-content);
  position: absolute;
}
#lanyard_root * .before\:ketch-left-1::before {
  content: var(--tw-content);
  left: 4px;
}
#lanyard_root * .before\:ketch-top-1::before {
  content: var(--tw-content);
  top: 4px;
}
#lanyard_root * .before\:ketch-h-2::before {
  content: var(--tw-content);
  height: 8px;
}
#lanyard_root * .before\:ketch-w-2::before {
  content: var(--tw-content);
  width: 8px;
}
#lanyard_root * .before\:ketch-rounded-full::before {
  content: var(--tw-content);
  border-radius: 9999px;
}
#lanyard_root * .before\:ketch-bg-white::before {
  content: var(--tw-content);
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}
#lanyard_root * .before\:ketch-opacity-0::before {
  content: var(--tw-content);
  opacity: 0;
}
#lanyard_root * .before\:ketch-content-\[\'\'\]::before {
  --tw-content: '';
  content: var(--tw-content);
}
#lanyard_root * .after\:ketch-absolute::after {
  content: var(--tw-content);
  position: absolute;
}
#lanyard_root * .after\:-ketch-left-0\.5::after {
  content: var(--tw-content);
  left: -2px;
}
#lanyard_root * .after\:-ketch-top-0\.5::after {
  content: var(--tw-content);
  top: -2px;
}
#lanyard_root * .after\:ketch-left-0::after {
  content: var(--tw-content);
  left: 0;
}
#lanyard_root * .after\:ketch-top-0::after {
  content: var(--tw-content);
  top: 0;
}
#lanyard_root * .after\:ketch-h-5::after {
  content: var(--tw-content);
  height: 20px;
}
#lanyard_root * .after\:ketch-w-5::after {
  content: var(--tw-content);
  width: 20px;
}
#lanyard_root * .after\:ketch-cursor-pointer::after {
  content: var(--tw-content);
  cursor: pointer;
}
#lanyard_root * .after\:ketch-rounded-\[3px\]::after {
  content: var(--tw-content);
  border-radius: 3px;
}
#lanyard_root * .after\:ketch-rounded-full::after {
  content: var(--tw-content);
  border-radius: 9999px;
}
#lanyard_root * .after\:ketch-content-\[\'\'\]::after {
  --tw-content: '';
  content: var(--tw-content);
}
#lanyard_root * .odd\:ketch-bg-white:nth-child(odd) {
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}
#lanyard_root * .even\:ketch-bg-gray-100:nth-child(even) {
  --tw-bg-opacity: 1;
  background-color: rgb(243 244 246 / var(--tw-bg-opacity));
}
#lanyard_root * .autofill\:\!ketch-shadow-\[inset_0_0_0px_1000px_var\(--k-preference-tabs-requests-rightForm-form-fields-inactive-background-color\)\]:-webkit-autofill {
  --tw-shadow: inset 0 0 0px 1000px var(--k-preference-tabs-requests-rightForm-form-fields-inactive-background-color) !important;
  --tw-shadow-colored: inset 0 0 0px 1000px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}
#lanyard_root * .autofill\:\!ketch-shadow-\[inset_0_0_0px_1000px_var\(--k-preference-tabs-requests-rightForm-form-fields-inactive-background-color\)\]:autofill {
  --tw-shadow: inset 0 0 0px 1000px var(--k-preference-tabs-requests-rightForm-form-fields-inactive-background-color) !important;
  --tw-shadow-colored: inset 0 0 0px 1000px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}
#lanyard_root * .hover\:ketch-cursor-pointer:hover {
  cursor: pointer;
}
#lanyard_root * .hover\:ketch-border-ketch-black-black-56:hover {
  border-color: rgba(7, 26, 36, 0.56);
}
#lanyard_root * .hover\:ketch-bg-gradient-to-r:hover {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * .hover\:ketch-from-states-hover-darken:hover {
  --tw-gradient-from: rgba(7, 26, 36, 0.10) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * .hover\:ketch-to-states-hover-darken:hover {
  --tw-gradient-to: rgba(7, 26, 36, 0.10) var(--tw-gradient-to-position);
}
#lanyard_root * .hover\:ketch-text-inherit:hover {
  color: inherit;
}
#lanyard_root * .focus\:ketch-border-none:focus {
  border-style: none;
}
#lanyard_root * .focus\:ketch-outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}
#lanyard_root * .focus-visible\:ketch-mb-1:focus-visible {
  margin-bottom: 4px;
}
#lanyard_root * .focus-visible\:\!ketch-border-\[--k-preference-tabs-requests-rightForm-form-fields-active-outline-color\]:focus-visible {
  border-color: var(--k-preference-tabs-requests-rightForm-form-fields-active-outline-color) !important;
}
#lanyard_root * .focus-visible\:ketch-border-blue-600:focus-visible {
  --tw-border-opacity: 1;
  border-color: rgb(37 99 235 / var(--tw-border-opacity));
}
#lanyard_root * .focus-visible\:\!ketch-bg-\[--k-preference-tabs-requests-rightForm-form-fields-active-background-color\]:focus-visible {
  background-color: var(--k-preference-tabs-requests-rightForm-form-fields-active-background-color) !important;
}
#lanyard_root * .focus-visible\:ketch-bg-gradient-to-r:focus-visible {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * .focus-visible\:ketch-from-states-focus-darken:focus-visible {
  --tw-gradient-from: rgba(7, 26, 36, 0.08) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * .focus-visible\:ketch-to-states-focus-darken:focus-visible {
  --tw-gradient-to: rgba(7, 26, 36, 0.08) var(--tw-gradient-to-position);
}
#lanyard_root * .focus-visible\:ketch-outline-none:focus-visible {
  outline: 2px solid transparent;
  outline-offset: 2px;
}
#lanyard_root * .focus-visible\:\!ketch-outline:focus-visible {
  outline-style: solid !important;
}
#lanyard_root * .focus-visible\:ketch-outline:focus-visible {
  outline-style: solid;
}
#lanyard_root * .focus-visible\:ketch-outline-2:focus-visible {
  outline-width: 2px;
}
#lanyard_root * .focus-visible\:\!ketch-outline-offset-2:focus-visible {
  outline-offset: 2px !important;
}
#lanyard_root * .focus-visible\:ketch-outline-offset-0:focus-visible {
  outline-offset: 0px;
}
#lanyard_root * .focus-visible\:ketch-outline-offset-2:focus-visible {
  outline-offset: 2px;
}
#lanyard_root * .focus-visible\:\!ketch-outline-\[--k-banner-header-returnButton-background-color\]:focus-visible {
  outline-color: var(--k-banner-header-returnButton-background-color) !important;
}
#lanyard_root * .focus-visible\:\!ketch-outline-\[--k-preference-tabs-requests-submitted-footer-actionButton-outline-color\]:focus-visible {
  outline-color: var(--k-preference-tabs-requests-submitted-footer-actionButton-outline-color) !important;
}
#lanyard_root * .focus-visible\:ketch-outline-default-outline:focus-visible {
  outline-color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * .focus-visible\:ketch-outline-inherit:focus-visible {
  outline-color: inherit;
}
#lanyard_root * .focus-visible\:ketch-outline-ketch-black-black-100:focus-visible {
  outline-color: rgba(7, 26, 36, 1);
}
#lanyard_root * .focus-visible\:ketch-outline-white:focus-visible {
  outline-color: #fff;
}
#lanyard_root * .focus-visible\:-webkit-autofill\:\!ketch-shadow-\[inset_0_0_0px_1000px_var\(--k-preference-tabs-requests-rightForm-form-fields-active-background-color\)\]:-webkit-autofill:focus-visible {
  --tw-shadow: inset 0 0 0px 1000px var(--k-preference-tabs-requests-rightForm-form-fields-active-background-color) !important;
  --tw-shadow-colored: inset 0 0 0px 1000px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}
#lanyard_root * .focus-visible\:autofill\:\!ketch-shadow-\[inset_0_0_0px_1000px_var\(--k-preference-tabs-requests-rightForm-form-fields-active-background-color\)\]:autofill:focus-visible {
  --tw-shadow: inset 0 0 0px 1000px var(--k-preference-tabs-requests-rightForm-form-fields-active-background-color) !important;
  --tw-shadow-colored: inset 0 0 0px 1000px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}
#lanyard_root * .focus-visible\:-webkit-autofill\:\!ketch-shadow-\[inset_0_0_0px_1000px_var\(--k-preference-tabs-requests-rightForm-form-fields-error-background-color\)\]:-webkit-autofill:focus-visible {
  --tw-shadow: inset 0 0 0px 1000px var(--k-preference-tabs-requests-rightForm-form-fields-error-background-color) !important;
  --tw-shadow-colored: inset 0 0 0px 1000px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}
#lanyard_root * .focus-visible\:autofill\:\!ketch-shadow-\[inset_0_0_0px_1000px_var\(--k-preference-tabs-requests-rightForm-form-fields-error-background-color\)\]:autofill:focus-visible {
  --tw-shadow: inset 0 0 0px 1000px var(--k-preference-tabs-requests-rightForm-form-fields-error-background-color) !important;
  --tw-shadow-colored: inset 0 0 0px 1000px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}
#lanyard_root * .active\:ketch-bg-gradient-to-r:active {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * .active\:ketch-from-states-pressed-darken:active {
  --tw-gradient-from: rgba(7, 26, 36, 0.24) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * .active\:ketch-to-states-pressed-darken:active {
  --tw-gradient-to: rgba(7, 26, 36, 0.24) var(--tw-gradient-to-position);
}
#lanyard_root * .disabled\:ketch-pointer-events-none:disabled {
  pointer-events: none;
}
#lanyard_root * .disabled\:ketch-cursor-not-allowed:disabled {
  cursor: not-allowed;
}
#lanyard_root * .disabled\:ketch-select-none:disabled {
  -webkit-user-select: none;
     -moz-user-select: none;
          user-select: none;
}
#lanyard_root * .disabled\:ketch-opacity-\[\.24\]:disabled {
  opacity: .24;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-flex) {
  display: flex;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-inline-flex) {
  display: inline-flex;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-hidden) {
  display: none;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-rounded-\[3px\]) {
  border-radius: 3px;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-rounded-full) {
  border-radius: 9999px;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-border-\[--k-consentGate-consentBlock-purposes-list-switchButtons-on-background-color\]) {
  border-color: var(--k-consentGate-consentBlock-purposes-list-switchButtons-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-border-\[--k-modal-purposeList-switchButtons-on-background-color\]) {
  border-color: var(--k-modal-purposeList-switchButtons-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-border-\[--k-preference-tabs-purposes-purposeList-switchButtons-on-background-color\]) {
  border-color: var(--k-preference-tabs-purposes-purposeList-switchButtons-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-border-\[--k-preference-tabs-requests-rightForm-form-checkboxes-selected-background-color\]) {
  border-color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-selected-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-border-\[--k-preference-tabs-subscriptions-list-checkbox-selected-background-color\]) {
  border-color: var(--k-preference-tabs-subscriptions-list-checkbox-selected-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-border-black) {
  --tw-border-opacity: 1;
  border-color: rgb(0 0 0 / var(--tw-border-opacity));
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-consentGate-consentBlock-purposes-list-switchButtons-on-background-color\]) {
  background-color: var(--k-consentGate-consentBlock-purposes-list-switchButtons-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-modal-purposeList-switchButtons-on-background-color\]) {
  background-color: var(--k-modal-purposeList-switchButtons-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-preference-tabs-purposes-purposeList-switchButtons-on-background-color\]) {
  background-color: var(--k-preference-tabs-purposes-purposeList-switchButtons-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-preference-tabs-requests-rightForm-form-checkboxes-selected-background-color\]) {
  background-color: var(--k-preference-tabs-requests-rightForm-form-checkboxes-selected-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-preference-tabs-subscriptions-list-checkbox-selected-background-color\]) {
  background-color: var(--k-preference-tabs-subscriptions-list-checkbox-selected-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-preference-tabs-subscriptions-list-switchButton-on-background-color\]) {
  background-color: var(--k-preference-tabs-subscriptions-list-switchButton-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:\!ketch-bg-\[--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-on-background-color\]) {
  background-color: var(--k-preference-tabs-subscriptions-unsubscribeAll-switchButton-on-background-color) !important;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-bg-black) {
  --tw-bg-opacity: 1;
  background-color: rgb(0 0 0 / var(--tw-bg-opacity));
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:ketch-font-semibold) {
  font-weight: 600;
}
#lanyard_root * :is(.ketch-peer:checked ~ .peer-checked\:before\:ketch-opacity-100)::before {
  content: var(--tw-content);
  opacity: 1;
}
#lanyard_root * :is(.ketch-peer:hover ~ .peer-hover\:ketch-bg-gradient-to-r) {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * :is(.ketch-peer:hover ~ .peer-hover\:ketch-from-states-hover-darken) {
  --tw-gradient-from: rgba(7, 26, 36, 0.10) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * :is(.ketch-peer:hover ~ .peer-hover\:ketch-to-states-hover-darken) {
  --tw-gradient-to: rgba(7, 26, 36, 0.10) var(--tw-gradient-to-position);
}
#lanyard_root * :is(.ketch-peer:hover ~ .peer-hover\:after\:ketch-bg-gradient-to-r)::after {
  content: var(--tw-content);
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * :is(.ketch-peer:hover ~ .peer-hover\:after\:ketch-from-states-hover-darken)::after {
  content: var(--tw-content);
  --tw-gradient-from: rgba(7, 26, 36, 0.10) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * :is(.ketch-peer:hover ~ .peer-hover\:after\:ketch-to-states-hover-darken)::after {
  content: var(--tw-content);
  --tw-gradient-to: rgba(7, 26, 36, 0.10) var(--tw-gradient-to-position);
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-bg-gradient-to-r) {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-from-states-focus-darken) {
  --tw-gradient-from: rgba(7, 26, 36, 0.08) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-to-states-focus-darken) {
  --tw-gradient-to: rgba(7, 26, 36, 0.08) var(--tw-gradient-to-position);
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-outline) {
  outline-style: solid;
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-outline-2) {
  outline-width: 2px;
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-outline-offset-2) {
  outline-offset: 2px;
}
#lanyard_root * :is(.ketch-peer:focus-visible ~ .peer-focus-visible\:ketch-outline-default-outline) {
  outline-color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * :is(.ketch-peer:focus-visible:checked ~ .peer-focus-visible\:peer-checked\:ketch-outline-black) {
  outline-color: #000;
}
#lanyard_root * :is(.ketch-peer:focus-visible:checked ~ .peer-focus-visible\:peer-checked\:ketch-outline-default-outline) {
  outline-color: rgba(7, 26, 36, 0.48);
}
#lanyard_root * :is(.ketch-peer:checked:focus-visible ~ .peer-checked\:peer-focus-visible\:after\:ketch-bg-gradient-to-r)::after {
  content: var(--tw-content);
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * :is(.ketch-peer:checked:focus-visible ~ .peer-checked\:peer-focus-visible\:after\:ketch-from-states-focus-darken)::after {
  content: var(--tw-content);
  --tw-gradient-from: rgba(7, 26, 36, 0.08) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * :is(.ketch-peer:checked:focus-visible ~ .peer-checked\:peer-focus-visible\:after\:ketch-to-states-focus-darken)::after {
  content: var(--tw-content);
  --tw-gradient-to: rgba(7, 26, 36, 0.08) var(--tw-gradient-to-position);
}
#lanyard_root * :is(.ketch-peer:active ~ .peer-active\:ketch-bg-gradient-to-r) {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * :is(.ketch-peer:active ~ .peer-active\:ketch-from-states-pressed-darken) {
  --tw-gradient-from: rgba(7, 26, 36, 0.24) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * :is(.ketch-peer:active ~ .peer-active\:ketch-to-states-pressed-darken) {
  --tw-gradient-to: rgba(7, 26, 36, 0.24) var(--tw-gradient-to-position);
}
#lanyard_root * :is(.ketch-peer:checked:active ~ .peer-checked\:peer-active\:after\:ketch-bg-gradient-to-r)::after {
  content: var(--tw-content);
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
#lanyard_root * :is(.ketch-peer:checked:active ~ .peer-checked\:peer-active\:after\:ketch-from-states-pressed-darken)::after {
  content: var(--tw-content);
  --tw-gradient-from: rgba(7, 26, 36, 0.24) var(--tw-gradient-from-position);
  --tw-gradient-to: rgba(7, 26, 36, 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
#lanyard_root * :is(.ketch-peer:checked:active ~ .peer-checked\:peer-active\:after\:ketch-to-states-pressed-darken)::after {
  content: var(--tw-content);
  --tw-gradient-to: rgba(7, 26, 36, 0.24) var(--tw-gradient-to-position);
}
#lanyard_root * :is(.ketch-peer:disabled ~ .peer-disabled\:ketch-pointer-events-none) {
  pointer-events: none;
}
#lanyard_root * :is(.ketch-peer:disabled ~ .peer-disabled\:ketch-cursor-not-allowed) {
  cursor: not-allowed;
}
#lanyard_root * :is(.ketch-peer:disabled ~ .peer-disabled\:ketch-select-none) {
  -webkit-user-select: none;
     -moz-user-select: none;
          user-select: none;
}
#lanyard_root * :is(.ketch-peer:disabled ~ .peer-disabled\:ketch-opacity-\[\.24\]) {
  opacity: .24;
}
#lanyard_root * :is(.ketch-peer:disabled:hover ~ .peer-disabled\:peer-hover\:ketch-bg-none) {
  background-image: none;
}
#lanyard_root * :is(.ketch-peer:disabled:hover ~ .peer-disabled\:peer-hover\:after\:ketch-bg-none)::after {
  content: var(--tw-content);
  background-image: none;
}
#lanyard_root * :is(.ketch-peer:disabled:focus-visible ~ .peer-disabled\:peer-focus-visible\:ketch-bg-none) {
  background-image: none;
}
#lanyard_root * :is(.ketch-peer:disabled:focus-visible ~ .peer-disabled\:peer-focus-visible\:after\:ketch-bg-none)::after {
  content: var(--tw-content);
  background-image: none;
}
#lanyard_root * :is(.ketch-peer:disabled:active ~ .peer-disabled\:peer-active\:ketch-bg-none) {
  background-image: none;
}
#lanyard_root * :is(.ketch-peer:disabled:active ~ .peer-disabled\:peer-active\:after\:ketch-bg-none)::after {
  content: var(--tw-content);
  background-image: none;
}
#lanyard_root * .aria-selected\:\!ketch-bg-\[--k-preference-navigation-layout-item-selectedBackground-color\][aria-selected="true"] {
  background-color: var(--k-preference-navigation-layout-item-selectedBackground-color) !important;
}
#lanyard_root * .aria-selected\:\!ketch-text-\[--k-preference-navigation-layout-item-selectedText-color\][aria-selected="true"] {
  color: var(--k-preference-navigation-layout-item-selectedText-color) !important;
}
#lanyard_root * .aria-selected\:ketch-underline[aria-selected="true"] {
  text-decoration-line: underline;
}
@media not all and (min-width: 480px) {
  #lanyard_root * .max-sm\:ketch-overflow-y-scroll {
    overflow-y: scroll;
  }
}
@media (min-width: 420px) {
  #lanyard_root * .xs\:ketch-bottom-1 {
    bottom: 4px;
  }
  #lanyard_root * .xs\:ketch-right-1 {
    right: 4px;
  }
  #lanyard_root * .xs\:ketch-right-auto {
    right: auto;
  }
  #lanyard_root * .xs\:ketch-top-1 {
    top: 4px;
  }
  #lanyard_root * .xs\:ketch-flex {
    display: flex;
  }
  #lanyard_root * .xs\:ketch-hidden {
    display: none;
  }
  #lanyard_root * .xs\:ketch-max-h-\[calc\(100dvh-8px\)\] {
    max-height: calc(100dvh - 8px);
  }
  #lanyard_root * .xs\:ketch-min-h-\[calc\(100dvh-8px\)\] {
    min-height: calc(100dvh - 8px);
  }
  #lanyard_root * .xs\:ketch-w-\[420px\] {
    width: 420px;
  }
  #lanyard_root * .xs\:ketch-w-\[calc\(100\%-8px\)\] {
    width: calc(100% - 8px);
  }
  #lanyard_root * .xs\:ketch-w-auto {
    width: auto;
  }
  #lanyard_root * .xs\:ketch-w-fit {
    width: -moz-fit-content;
    width: fit-content;
  }
  #lanyard_root * .xs\:ketch-w-full {
    width: 100%;
  }
  #lanyard_root * .xs\:ketch-max-w-\[184px\] {
    max-width: 184px;
  }
  #lanyard_root * .xs\:ketch-translate-y-0 {
    --tw-translate-y: 0;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
  }
  #lanyard_root * .xs\:ketch-flex-row {
    flex-direction: row;
  }
  #lanyard_root * .xs\:ketch-items-center {
    align-items: center;
  }
  #lanyard_root * .xs\:ketch-gap-0 {
    gap: 0;
  }
  #lanyard_root * .xs\:ketch-px-6 {
    padding-left: 24px;
    padding-right: 24px;
  }
  #lanyard_root * .xs\:ketch-py-5 {
    padding-top: 20px;
    padding-bottom: 20px;
  }
  #lanyard_root * .xs\:ketch-text-ketch-h1-small {
    font-size: 26px;
    line-height: 36.4px;
  }
}
@media (min-width: 480px) {
  #lanyard_root * .sm\:ketch-left-2\/4 {
    left: 50%;
  }
  #lanyard_root * .sm\:ketch-flex {
    display: flex;
  }
  #lanyard_root * .sm\:ketch-hidden {
    display: none;
  }
  #lanyard_root * .sm\:ketch-max-h-\[calc\(100dvh-8px\)\] {
    max-height: calc(100dvh - 8px);
  }
  #lanyard_root * .sm\:ketch-max-h-dvh {
    max-height: 100dvh;
  }
  #lanyard_root * .sm\:ketch-w-\[730px\] {
    width: 730px;
  }
  #lanyard_root * .sm\:ketch-w-auto {
    width: auto;
  }
  #lanyard_root * .sm\:ketch-w-fit {
    width: -moz-fit-content;
    width: fit-content;
  }
  #lanyard_root * .sm\:ketch-w-full {
    width: 100%;
  }
  #lanyard_root * .sm\:\!ketch-max-w-\[calc\(75\%\+var\(--safe-area-inset-left\)\+var\(--safe-area-inset-right\)\)\] {
    max-width: calc(75% + var(--safe-area-inset-left) + var(--safe-area-inset-right)) !important;
  }
  #lanyard_root * .sm\:ketch-max-w-\[184px\] {
    max-width: 184px;
  }
  #lanyard_root * .sm\:ketch-max-w-\[328px\] {
    max-width: 328px;
  }
  #lanyard_root * .sm\:ketch-max-w-\[40\%\] {
    max-width: 40%;
  }
  #lanyard_root * .sm\:ketch-max-w-\[calc\(100\%-8px\)\] {
    max-width: calc(100% - 8px);
  }
  #lanyard_root * .sm\:ketch-max-w-\[calc\(80\%\+var\(--safe-area-inset-left\)\+var\(--safe-area-inset-right\)\)\] {
    max-width: calc(80% + var(--safe-area-inset-left) + var(--safe-area-inset-right));
  }
  #lanyard_root * .sm\:-ketch-translate-x-2\/4 {
    --tw-translate-x: -50%;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
  }
  #lanyard_root * .sm\:ketch-flex-row {
    flex-direction: row;
  }
  #lanyard_root * .sm\:ketch-flex-col {
    flex-direction: column;
  }
  #lanyard_root * .sm\:ketch-items-end {
    align-items: flex-end;
  }
  #lanyard_root * .sm\:ketch-items-center {
    align-items: center;
  }
  #lanyard_root * .sm\:ketch-items-stretch {
    align-items: stretch;
  }
  #lanyard_root * .sm\:ketch-gap-0 {
    gap: 0;
  }
  #lanyard_root * .sm\:ketch-gap-6 {
    gap: 24px;
  }
  #lanyard_root * .sm\:ketch-gap-8 {
    gap: 32px;
  }
  #lanyard_root * .sm\:ketch-overflow-visible {
    overflow: visible;
  }
  #lanyard_root * .sm\:ketch-overflow-y-scroll {
    overflow-y: scroll;
  }
  #lanyard_root * .sm\:ketch-px-6 {
    padding-left: 24px;
    padding-right: 24px;
  }
  #lanyard_root * .sm\:ketch-py-5 {
    padding-top: 20px;
    padding-bottom: 20px;
  }
  #lanyard_root * .sm\:ketch-text-center {
    text-align: center;
  }
  #lanyard_root * .sm\:ketch-text-ketch-h1-small {
    font-size: 26px;
    line-height: 36.4px;
  }
}
@media (min-width: 769px) {
  #lanyard_root * .md\:ketch-mx-auto {
    margin-left: auto;
    margin-right: auto;
  }
  #lanyard_root * .md\:ketch-block {
    display: block;
  }
  #lanyard_root * .md\:ketch-inline-block {
    display: inline-block;
  }
  #lanyard_root * .md\:ketch-flex {
    display: flex;
  }
  #lanyard_root * .md\:ketch-inline-flex {
    display: inline-flex;
  }
  #lanyard_root * .md\:ketch-hidden {
    display: none;
  }
  #lanyard_root * .md\:ketch-h-16 {
    height: 64px;
  }
  #lanyard_root * .md\:ketch-max-h-80 {
    max-height: 320px;
  }
  #lanyard_root * .md\:ketch-max-w-\[50\%\] {
    max-width: 50%;
  }
  #lanyard_root * .md\:ketch-grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
  #lanyard_root * .md\:ketch-grid-cols-\[160px_1fr\] {
    grid-template-columns: 160px 1fr;
  }
  #lanyard_root * .md\:ketch-grid-cols-\[328px_1fr\] {
    grid-template-columns: 328px 1fr;
  }
  #lanyard_root * .md\:ketch-flex-row {
    flex-direction: row;
  }
  #lanyard_root * .md\:ketch-flex-col {
    flex-direction: column;
  }
  #lanyard_root * .md\:ketch-items-start {
    align-items: flex-start;
  }
  #lanyard_root * .md\:ketch-items-center {
    align-items: center;
  }
  #lanyard_root * .md\:ketch-justify-between {
    justify-content: space-between;
  }
  #lanyard_root * .md\:ketch-gap-4 {
    gap: 16px;
  }
  #lanyard_root * .md\:ketch-gap-6 {
    gap: 24px;
  }
  #lanyard_root * .md\:ketch-gap-8 {
    gap: 32px;
  }
  #lanyard_root * .md\:ketch-px-0 {
    padding-left: 0;
    padding-right: 0;
  }
  #lanyard_root * .md\:ketch-px-4 {
    padding-left: 16px;
    padding-right: 16px;
  }
  #lanyard_root * .md\:ketch-px-8 {
    padding-left: 32px;
    padding-right: 32px;
  }
  #lanyard_root * .md\:ketch-pb-0 {
    padding-bottom: 0;
  }
  #lanyard_root * .md\:ketch-pb-6 {
    padding-bottom: 24px;
  }
  #lanyard_root * .md\:ketch-pl-8 {
    padding-left: 32px;
  }
  #lanyard_root * .md\:ketch-pr-0 {
    padding-right: 0;
  }
  #lanyard_root * .md\:ketch-pr-3 {
    padding-right: 12px;
  }
  #lanyard_root * .md\:ketch-pr-4 {
    padding-right: 16px;
  }
  #lanyard_root * .md\:ketch-pt-8 {
    padding-top: 32px;
  }
  #lanyard_root * .md\:ketch-text-center {
    text-align: center;
  }
  #lanyard_root * .md\:ketch-text-ketch-m {
    font-size: 13px;
    line-height: 16px;
  }
}
@media (min-width: 1024px) {
  #lanyard_root * .lm\:ketch-col-span-1 {
    grid-column: span 1 / span 1;
  }
  #lanyard_root * .lm\:ketch-max-h-\[90\%\] {
    max-height: 90%;
  }
  #lanyard_root * .lm\:ketch-min-h-0 {
    min-height: 0;
  }
  #lanyard_root * .lm\:ketch-min-h-10 {
    min-height: 40px;
  }
  #lanyard_root * .lm\:ketch-min-h-12 {
    min-height: 48px;
  }
  #lanyard_root * .lm\:ketch-px-4 {
    padding-left: 16px;
    padding-right: 16px;
  }
  #lanyard_root * .lm\:ketch-text-ketch-h4 {
    font-size: 16px;
    line-height: 24px;
  }
  #lanyard_root * .lm\:ketch-text-ketch-l {
    font-size: 14px;
    line-height: 21px;
  }
  #lanyard_root * .lm\:ketch-text-ketch-lm {
    font-size: 14px;
    line-height: 21px;
  }
}
@media (min-width: 1440px) {
  #lanyard_root * .lg\:ketch-mx-auto {
    margin-left: auto;
    margin-right: auto;
  }
  #lanyard_root * .lg\:ketch-max-h-\[480px\] {
    max-height: 480px;
  }
  #lanyard_root * .lg\:ketch-px-0 {
    padding-left: 0;
    padding-right: 0;
  }
  #lanyard_root * .lg\:ketch-pr-0 {
    padding-right: 0;
  }
  #lanyard_root * .lg\:ketch-pr-14 {
    padding-right: 56px;
  }
  #lanyard_root * .lg\:ketch-pr-\[72px\] {
    padding-right: 72px;
  }
}
</style><style>@media (min-width: 1920px) {
  #lanyard_root[data-screen*="TIZEN"] {
    /* Zoom in fonts for high res TV screens */
    zoom: 110%;
  }

    /* TIZEN has partial support for outline-color & focus-visible */
    @supports not (outline-color: #9c63ff) {
  #lanyard_root[data-screen*="TIZEN"] {
      /* Remove :focus styles when running on modern browsers with support for :focus-visible */
  }
      #lanyard_root[data-screen*="TIZEN"] *:focus { border: 3px solid #9c63ff; }
      #lanyard_root[data-screen*="TIZEN"] *:focus:not(:focus-visible) { border: none; }
      #lanyard_root[data-screen*="TIZEN"] *:focus-visible { border: 3px solid #9c63ff; }
    }
    @supports (outline-color: #9c63ff) {
  #lanyard_root[data-screen*="TIZEN"] {
      /* Remove :focus styles when running on modern browsers with support for :focus-visible */
  }
      #lanyard_root[data-screen*="TIZEN"] *:focus { outline: 3px solid #9c63ff; }
      #lanyard_root[data-screen*="TIZEN"] *:focus:not(:focus-visible) { outline: none; }
      #lanyard_root[data-screen*="TIZEN"] *:focus-visible { outline: 3px solid #9c63ff; }
    }
}
</style><style>.root__A7aXF{text-align:left}.root__A7aXF *{-webkit-box-sizing:border-box;box-sizing:border-box;font-family:Arial,Helvetica,sans-serif;font-weight:normal}</style><style>.root__H_E27{margin:0;position:fixed;width:48px;height:48px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;border:none;border-radius:50%;-webkit-box-shadow:none;box-shadow:none;cursor:pointer;overflow:hidden;-webkit-transition:opacity .25s linear;transition:opacity .25s linear;z-index:2147483647}.root__H_E27:hover{opacity:.9}.icon__HrAtF{max-width:32px;max-height:32px}.bottomRight__ILequ{right:16px;bottom:16px}.bottomLeft__iB1Ik{left:16px;bottom:16px}</style><script src="https://securepubads.g.doubleclick.net/gampad/adx?iu=/6581/web/it/video_player/weather/local_home&amp;sz=3x3&amp;c=1776679085849&amp;m=text/javascript&amp;t=fdate%3D20260420%26lang%3Dit%26ut%3D1%26advelvet%3D5%26inview%3Dititrome213490weather-forecast213490%253Awbr%252Cwb%26bot%3D0%26pgview%3D1%26partner%3Dgoogle_search_accuweather%26ufdb%3DLII7%26city%3DRome%26country%3DIT%26state%3D62%26dma%3Dnull%26key%3D213490%26region%3Deur%26lat%3D41.901%26lon%3D12.48%26browser%3Dsafari%26connection%3Dmobile_vhigh_5000%26wx_seg%3D101100100%252C102102102%252C109101100%252C108102100%252C100108101%252C102100100%252C102101100%252C102103100%252C107100102%252C100111100%252C107101102%252C108103101%252C101103100%252C100113103%252C108104101%252C101105100%252C110100100%252C109104100%252C109105100%252C100106102%252C110101101%252C109100102%252C108101102%252C103100102%252C109103102%252C103101102%252C101106102%252C108100102%252C100109105%252C102104102%252C104100103%252C101104101%252C104101101%252C100109102%252C109102102%252C100114105%252C109106102%252C101107101%252C101108101%252C101102102%252C105100102%252C107103102%252C100114102%252C100114101%252C101101101%26alertscategory%3DSEVERE%252CSEVERE%26alertssource%3Dit%252Cit%26alertstypeid%3DIT312%252CIT312%26cuhd%3D64%26cuhi%3D67%26cuuv%3D6%26cuwd%3D8%26cuwx%3D3%26realfeel%3D75%252Ca80%252Cb75%252Cc75%252Cd75%26cuaq%3D3%26fc1hi%3D74%26fc1lo%3D54%26fc1wx%3D2%26lfscategory%3Drain%26lfsday%3D3%26lfsseverity%3D5%26lfs%3D5_rain_3%26pt%3D15918%26userid%3Dactive%26userid3p%3Dmissing%26sub%3Dfree%26auth%3Dfalse%26site%3Ddesktop%26hour%3D11%26viewport%3D1470x840%26iabctax%3DIAB15-10%252CIAB20-14%252CIAB20-19%252C390%252C659%26from%3Dnull&amp;ppid=7d695715xd89fx4158xab9bx5114c8ba51db&amp;userid3p=missing" id="videoPlayerAdUnitScript" async=""></script><script esp-signal="true" src="https://ads.pubmatic.com/AdServer/js/google-esp.js"></script><script esp-signal="true" src="https://invstatic101.creativecdn.com/encrypted-signals/encrypted-tag-g.js"></script><script esp-signal="true" src="https://oa.openxcdn.net/esp.js"></script><script esp-signal="true" src="https://cdn.id5-sync.com/api/1.0/esp.js"></script><script esp-signal="true" src="https://connectid.analytics.yahoo.com/connectId-gpt.js"></script><script esp-signal="true" src="https://static.criteo.net/js/ld/publishertag.ids.js"></script><script esp-signal="true" src="https://tags.crwdcntrl.net/lt/c/16589/sync.min.js"></script><style id="fullscreenRadarAnchor" type="text/css">@media (max-width: 767px) {html:has(ins[data-anchor-shown="true"]) .map-container-legacy.full-screen {padding-top: 0px;top: 0px;} .map-container-legacy.full-screen .play-bar{bottom:60px}}</style><script src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5771594739411148" id="google_adsense_script" async="" data-checked-head="true"></script><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9nrunKdU5m96PSN1XsSGr3qOP0lvPFUB2AiAylCDlN5DTl17uDFkpQuHj1AFtgWLxpLaiBZuhrtb2WOu7ofHwEAAACKeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiQUlQcm9tcHRBUElNdWx0aW1vZGFsSW5wdXQiLCJleHBpcnkiOjE3NzQzMTA0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A93bovR+QVXNx2/38qDbmeYYf1wdte9EO37K9eMq3r+541qo0byhYU899BhPB7Cv9QqD7wIbR1B6OAc9kEfYCA4AAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiQUlQcm9tcHRBUElNdWx0aW1vZGFsSW5wdXQiLCJleHBpcnkiOjE3NzQzMTA0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A1S5fojrAunSDrFbD8OfGmFHdRFZymSM/1ss3G+NEttCLfHkXvlcF6LGLH8Mo5PakLO1sCASXU1/gQf6XGuTBgwAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQUlQcm9tcHRBUElNdWx0aW1vZGFsSW5wdXQiLCJleHBpcnkiOjE3NzQzMTA0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"></head>

<body class="three-day    full-animation rfphrase-disabled" aria-hidden="false" style="">
	<div class="template-root" style="display:none">
		<div class="basic-header   " style="visibility: hidden;">

	<a href="/pwa" class="pwa-top-banner">
		<svg class="arrow-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><defs><path id="a" d="m8.495.505 5 5v.99l-5 5-.99-.99 3.805-3.806L0 6.7V5.3l11.31-.001-3.805-3.804.99-.99z"></path></defs><use fill="#fff" fill-rule="nonzero" xlink:href="#a" transform="translate(2 3)"></use></svg>
		Indietro
	</a>


	    <div class="nav-alert-container no-banners">
    </div>


	<div class="header-outer">
		<div class="header-inner">
			<a class="header-logo" href="/">
				<svg data-eager="" xmlns="http://www.w3.org/2000/svg" width="168" height="24" viewBox="0 0 168 24"><g clip-path="url(#clip0_1785_92941)"><path d="M163.324 20.2961V14.1771C163.324 12.9231 163.589 12.0833 164.119 11.6575C164.649 11.2318 165.501 11.0189 166.673 11.0189H167.805V8.2468H166.842C166.077 8.22951 165.316 8.36062 164.601 8.63286C164.017 8.85832 163.507 9.24234 163.129 9.74172L162.549 8.2468H160.38V20.2961H163.324ZM152.816 10.4877C153.652 10.4877 154.286 10.7287 154.72 11.2105C155.177 11.7511 155.432 12.4332 155.443 13.1408H149.971C149.982 12.4308 150.243 11.7475 150.708 11.2105C150.957 10.9599 151.257 10.7657 151.588 10.641C151.918 10.5163 152.272 10.464 152.624 10.4877H152.816ZM155.274 16.659C155.08 17.1042 154.752 17.4778 154.336 17.7281C153.92 17.9783 153.436 18.0926 152.952 18.0552H152.76C151.858 18.0552 151.181 17.8085 150.729 17.3092C150.252 16.7667 149.975 16.0773 149.945 15.3557H158.38V14.1278C158.38 12.2468 157.882 10.7441 156.885 9.6198C155.889 8.49547 154.534 7.9333 152.821 7.9333H152.63C150.908 7.9333 149.545 8.4916 148.543 9.6082C147.54 10.7248 147.038 12.1675 147.036 13.9362V14.7287C147.027 15.5424 147.163 16.3513 147.437 17.1176C147.681 17.8079 148.067 18.4397 148.569 18.9725C149.077 19.499 149.693 19.9099 150.374 20.1771C151.139 20.4754 151.954 20.6223 152.775 20.6096H152.967C153.976 20.6343 154.974 20.4026 155.869 19.9362C156.705 19.4714 157.391 18.7775 157.846 17.9362L155.274 16.659ZM137.199 20.2961V13.2599C137.186 12.5393 137.415 11.8354 137.849 11.2599C138.062 10.995 138.335 10.7847 138.645 10.6464C138.956 10.5081 139.295 10.4457 139.634 10.4645H139.924C140.217 10.4511 140.509 10.5001 140.781 10.6082C141.054 10.7163 141.3 10.8811 141.504 11.0915C141.898 11.5095 142.084 12.2004 142.084 13.1641V20.2961H145.051V12.6532C145.051 11.2395 144.659 10.0959 143.89 9.23083C143.501 8.79975 143.021 8.45953 142.486 8.23429C141.951 8.00906 141.373 7.90432 140.792 7.9275H140.456C139.833 7.92317 139.217 8.0508 138.647 8.30196C138.093 8.54218 137.598 8.8997 137.196 9.34985V3.42822H134.235V20.2961H137.199ZM129.44 17.6575C129.245 17.4892 129.149 17.1728 129.149 16.7054V10.6213H132.052V8.23519H129.149V5.58497H126.618L126.305 8.23519H124.34V10.6213H126.218V16.717C126.218 17.8259 126.483 18.6967 127.013 19.3295C127.543 19.9623 128.435 20.2787 129.689 20.2787H132.026V17.8927H130.316C130.005 17.917 129.696 17.8272 129.446 17.6401M117.129 18.0871C116.637 18.1193 116.147 17.9921 115.733 17.7243C115.575 17.6087 115.449 17.456 115.364 17.2798C115.28 17.1037 115.24 16.9094 115.248 16.7141V16.6154C115.245 16.4029 115.292 16.1927 115.386 16.0022C115.481 15.8118 115.62 15.6468 115.791 15.5211C116.155 15.2405 116.793 15.0992 117.707 15.0973H119.901V15.5559C119.901 16.4248 119.664 17.0673 119.19 17.4834C118.668 17.9181 118.002 18.1418 117.324 18.1104L117.129 18.0871ZM116.525 20.5922C117.236 20.6064 117.941 20.4585 118.586 20.1597C119.203 19.8575 119.725 19.3903 120.093 18.8099L120.601 20.2787H122.842V12.3919C122.842 10.8961 122.407 9.77172 121.538 9.01894C120.67 8.26615 119.457 7.88879 117.901 7.88685H117.611C116.215 7.88685 115.112 8.17713 114.311 8.74027C113.564 9.23427 113.011 9.97027 112.743 10.8245L115.356 11.8869C115.502 11.4815 115.766 11.1289 116.113 10.8738C116.539 10.5829 117.049 10.4392 117.565 10.4645H117.855C118.546 10.4645 119.06 10.6329 119.399 10.9696C119.574 11.1606 119.71 11.385 119.796 11.6293C119.883 11.8737 119.92 12.1331 119.904 12.3919V12.9957H117.75C115.983 12.9957 114.638 13.3411 113.713 14.032C113.272 14.3447 112.915 14.7613 112.673 15.2448C112.432 15.7283 112.313 16.2639 112.328 16.8041V16.9725C112.303 17.4653 112.383 17.9577 112.564 18.4169C112.744 18.876 113.021 19.2911 113.376 19.6343C114.074 20.2845 115.058 20.6096 116.328 20.6096L116.525 20.5922ZM105.393 10.4703C106.227 10.4703 106.862 10.7112 107.297 11.1931C107.753 11.7344 108.008 12.4161 108.02 13.1234H102.543C102.554 12.4139 102.814 11.731 103.277 11.1931C103.526 10.943 103.826 10.7491 104.157 10.6244C104.487 10.4997 104.841 10.4472 105.193 10.4703H105.393ZM107.852 16.6416C107.658 17.0867 107.33 17.4604 106.914 17.7106C106.498 17.9609 106.014 18.0752 105.53 18.0378H105.335C104.435 18.0378 103.756 17.7911 103.303 17.2918C102.827 16.7493 102.55 16.0598 102.52 15.3382H110.955V14.1104C110.955 12.2294 110.457 10.7267 109.46 9.60238C108.463 8.47805 107.109 7.91588 105.396 7.91588H105.181C103.463 7.91588 102.102 8.47419 101.097 9.59078C100.093 10.7074 99.5906 12.15 99.5906 13.9188V14.7112C99.582 15.5247 99.7166 16.3334 99.9883 17.1002C100.234 17.79 100.619 18.4215 101.12 18.9551C101.63 19.481 102.247 19.8918 102.929 20.1597C103.692 20.458 104.507 20.6049 105.326 20.5922H105.521C106.53 20.6169 107.529 20.3852 108.424 19.9188C109.259 19.4531 109.945 18.7594 110.401 17.9188L107.852 16.6416ZM85.4629 20.2787L88.9985 8.00877L92.3715 20.299H95.0711L99.9158 3.65464V3.43984H97.013L93.82 15.3673L90.6879 3.43984H87.4949L84.2031 15.5559L81.0885 3.42822H78.0319V3.65464L82.6763 20.3078L85.4629 20.2787ZM66.4237 8.22939V15.8694C66.4237 17.284 66.8108 18.4248 67.5848 19.2918C67.9752 19.7242 68.4563 20.065 68.9938 20.2898C69.5312 20.5146 70.1117 20.6179 70.6937 20.5922H71.0072C71.6954 20.6003 72.3762 20.4482 72.9956 20.1481C73.5931 19.8548 74.1101 19.4204 74.5021 18.8825L75.0072 20.2787H77.2249V8.2468H74.2728V15.2831C74.2854 16.0064 74.0521 16.7126 73.611 17.286C73.3946 17.55 73.1193 17.7594 72.8073 17.8976C72.4952 18.0357 72.155 18.0987 71.8142 18.0813H71.5239C71.2332 18.0927 70.9435 18.0427 70.6734 17.9347C70.4034 17.8267 70.159 17.663 69.9564 17.4543C69.5558 17.0364 69.3555 16.3455 69.3555 15.3818V8.2468L66.4237 8.22939ZM63.193 8.71125C62.3899 8.18294 61.3381 7.91782 60.0377 7.91588H59.8432C58.1248 7.91588 56.7634 8.42193 55.759 9.43403C54.7546 10.4461 54.2525 11.7959 54.2525 13.4834V15.0247C54.2525 16.7141 54.7546 18.0639 55.759 19.0741C56.7634 20.0842 58.1248 20.5903 59.8432 20.5922H60.0377C61.0687 20.6291 62.0911 20.3928 63.0014 19.9072C63.8122 19.4215 64.4584 18.7035 64.8562 17.8462L62.4208 16.4732C62.2315 16.9153 61.9316 17.3011 61.55 17.5937C61.1079 17.8938 60.58 18.0416 60.0464 18.0146H59.8519C58.9375 18.0146 58.2612 17.7243 57.82 17.1699C57.3631 16.5418 57.1329 15.7774 57.1668 15.0015V13.524C57.1297 12.7442 57.3602 11.975 57.82 11.344C58.2525 10.7896 58.9288 10.5139 59.8519 10.5139H60.0464C60.5919 10.4846 61.1311 10.6412 61.5761 10.958C61.9631 11.2752 62.2628 11.6858 62.447 12.151L65.0014 10.9464C64.635 10.0423 64.0048 9.26949 63.193 8.72866M51.312 8.72866C50.5089 8.20036 49.4562 7.93523 48.1538 7.9333H47.9622C46.2438 7.9333 44.8824 8.43935 43.878 9.45144C42.8737 10.4635 42.3715 11.8133 42.3715 13.5008V15.0422C42.3715 16.7316 42.8737 18.0813 43.878 19.0915C44.8824 20.1017 46.2438 20.6077 47.9622 20.6096H48.1538C49.1858 20.6468 50.2092 20.4104 51.1204 19.9246C51.9312 19.4389 52.5774 18.7209 52.9753 17.8636L50.5399 16.4906C50.3506 16.9327 50.0507 17.3185 49.669 17.6111C49.2261 17.9117 48.6971 18.0594 48.1625 18.032H47.9709C47.0536 18.032 46.3802 17.7417 45.939 17.1873C45.4844 16.5583 45.2553 15.7943 45.2888 15.0189V13.524C45.2522 12.7447 45.4815 11.976 45.939 11.344C46.3744 10.7896 47.0478 10.5139 47.9709 10.5139H48.1625C48.7089 10.4842 49.2492 10.6408 49.6951 10.958C50.0821 11.2752 50.3818 11.6858 50.566 12.151L53.1204 10.9464C52.754 10.0423 52.1238 9.26949 51.312 8.72866ZM34.4179 7.83751L36.4179 14.0552H32.3541L34.4179 7.83751ZM32.9956 3.42822L27.3875 20.0813V20.2961H30.3279L31.489 16.778H37.3207L38.4557 20.2961H41.5384V20.0813L35.9245 3.42822H32.9956Z" fill="white"></path><path d="M12.003 20.328C10.3574 20.3286 8.74871 19.8412 7.38022 18.9274C6.01174 18.0136 4.94498 16.7145 4.31487 15.1944C3.68475 13.6743 3.51959 12.0015 3.84027 10.3875C4.16094 8.7735 4.95305 7.29086 6.11641 6.1271C7.27977 4.96333 8.76212 4.1707 10.376 3.84947C11.9899 3.52823 13.6627 3.69281 15.1831 4.3224C16.7034 4.95198 18.0029 6.01828 18.9171 7.38645C19.8314 8.75462 20.3194 10.3632 20.3194 12.0087C20.3171 14.2139 19.4402 16.3282 17.8812 17.8878C16.3221 19.4474 14.2082 20.3249 12.003 20.328ZM24.0088 11.9681L21.2715 9.48912L22.3745 5.97678L18.7664 5.19303L17.971 1.59071L14.4587 2.71988L11.9681 0L9.48918 2.73439L5.97104 1.62264L5.1931 5.22496L1.59078 6.02322L2.71415 9.54136L-0.0057373 12.0319L2.72576 14.508L1.61691 18.0261L5.22213 18.8041L6.02039 22.4064L9.53273 21.2801L12.0262 24L14.5022 21.2656L18.0204 22.3774L18.7983 18.7721L22.4007 17.971L21.2918 14.4586L24.0088 11.9681Z" fill="#F05514"></path><path d="M6.75181 6.75475C7.78948 5.71723 9.1115 5.01071 10.5507 4.72452C11.9899 4.43833 13.4817 4.58532 14.8373 5.14691C16.193 5.7085 17.3517 6.65948 18.1669 7.87957C18.9821 9.09967 19.4172 10.5341 19.4172 12.0015C19.4172 13.4689 18.9821 14.9033 18.1669 16.1234C17.3517 17.3435 16.193 18.2945 14.8373 18.8561C13.4817 19.4176 11.9899 19.5646 10.5507 19.2785C9.1115 18.9923 7.78948 18.2857 6.75181 17.2482C5.36228 15.8556 4.58191 13.9687 4.58191 12.0015C4.58191 10.0342 5.36228 8.14733 6.75181 6.75475Z" fill="#F05514"></path><path d="M166.328 20.2961C166.139 20.3008 165.952 20.2488 165.792 20.1469C165.633 20.045 165.507 19.8978 165.432 19.7241C165.356 19.5504 165.334 19.3581 165.368 19.1719C165.403 18.9856 165.492 18.8138 165.624 18.6784C165.757 18.543 165.926 18.4502 166.112 18.4119C166.297 18.3736 166.49 18.3915 166.665 18.4632C166.841 18.535 166.991 18.6574 167.096 18.8148C167.201 18.9723 167.257 19.1575 167.257 19.3469C167.258 19.4703 167.235 19.5928 167.19 19.7073C167.144 19.8218 167.076 19.9262 166.989 20.0144C166.903 20.1025 166.8 20.1728 166.687 20.2212C166.573 20.2695 166.451 20.295 166.328 20.2961ZM166.328 18.5545C166.171 18.5481 166.016 18.5887 165.883 18.6711C165.749 18.7534 165.644 18.8738 165.579 19.0167C165.515 19.1595 165.494 19.3185 165.521 19.473C165.547 19.6276 165.619 19.7707 165.727 19.884C165.836 19.9974 165.975 20.0758 166.129 20.1091C166.282 20.1425 166.441 20.1293 166.587 20.0713C166.733 20.0132 166.858 19.913 166.946 19.7834C167.034 19.6538 167.082 19.5008 167.083 19.344C167.085 19.2427 167.068 19.1418 167.031 19.0472C166.995 18.9526 166.94 18.8663 166.87 18.7931C166.799 18.7199 166.715 18.6614 166.622 18.621C166.529 18.5805 166.429 18.5589 166.328 18.5574V18.5545ZM165.965 18.7867H166.31C166.578 18.7867 166.728 18.8999 166.728 19.1205V19.1466C166.733 19.212 166.717 19.2773 166.682 19.3327C166.647 19.3881 166.595 19.4308 166.534 19.4543L166.752 19.8549H166.511L166.319 19.4863H166.194V19.8549H165.965V18.7867ZM166.194 19.0015V19.2744H166.334C166.438 19.2744 166.496 19.2308 166.496 19.1408V19.1263C166.496 19.045 166.438 19.0015 166.334 19.0015H166.194Z" fill="white"></path></g><defs><clipPath id="clip0_1785_92941"><rect width="167.808" height="24" fill="white"></rect></clipPath></defs></svg>
			</a>

			
				<a class="header-city-link" href="/it/it/rome/213490/weather-forecast/213490">
					<h1 class="header-loc">Roma, Lazio</h1>
					<span class="header-temp">21°<span class="unit">C</span></span>
					<img class="header-weather-icon" src="/images/weathericons/v2a/03.svg" width="27" height="27">
				</a>

				
					
				
			

			<div class="pull-right">
				
					
					
						
						<div class="header-search-bar search-bar">
	<div class="searchbar-inner">
		<svg class="icon-search" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path transform="translate(3 3)" d="M7.186 13.554c-3.462 0-6.303-2.869-6.303-6.359C.883 3.681 3.724.837 7.186.837c3.437 0 6.278 2.844 6.278 6.358 0 3.49-2.865 6.359-6.278 6.359zm5.323-1.602a7.176 7.176 0 0 0 1.815-4.757c0-3.968-3.2-7.195-7.138-7.195C3.223 0 0 3.227 0 7.195c0 3.944 3.223 7.171 7.186 7.171a7.058 7.058 0 0 0 4.75-1.84L17.427 18l.573-.55-5.49-5.498z"></path></svg>
		<form class="search-form" action="/it/search-locations" method="GET">
			<input name="query" class="search-input" type="text" placeholder="Cerca" data-placeholder="Cerca" data-alternative-placeholder="Cerca" autocomplete="off">
		</form>
		<svg class="clear-icon close-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><g fill-rule="evenodd" transform="translate(-1 -1)"><rect width="2" height="24" x="9" y="-2" rx="1" transform="rotate(45 10 10)"></rect><rect width="2" height="24" x="9" y="-2" rx="1" transform="rotate(-45 10 10)"></rect></g></svg>
		
	</div>

	<div class="search-bar-dropdown">
		<div class="use-current-location">
			<svg class="icon-gps gps-icon" xmlns="http://www.w3.org/2000/svg" width="14" height="16" viewBox="0 0 14 16"><g id="Symbols" fill="#000" stroke="none" stroke-width="1" fill-rule="evenodd" fill-opacity="0.995941"><g id="ICONS-/-Menu-/-GPS"><polygon id="Triangle" transform="translate(9.446152, 7.361216) rotate(-330.000000) translate(-9.446152, -7.361216) " points="9.44615242 -1.13878407 15.4461524 15.8612159 9.44615242 12.4612159 3.44615242 15.8612159"></polygon></g></g></svg>
			<span>Usa località attuale</span>
		</div>
		
		<div class="recent-locations-dropdown">
			<div class="recent-title">Recenti</div>
				<a class="recent-location" data-location-key="213490" data-fetch="false" data-place-name="" href="/web-api/three-day-redirect?key=213490&amp;target=">
					<div class="recent-location__title-wrapper">
						<p class="recent-location__name">Roma</p>
						<p class="recent-location__admin">Lazio</p>
					</div>
					<img class="recent-location__icon" src="/images/weathericons/v2a/03.svg" width="32" height="32">
					<span class="recent-location__temp">21°</span>
				</a>
		</div>
		<div class="search-results">
			<div class="results-container"></div>
		</div>
		
		<div class="search-results no-search-result hidden">
			<div class="results-container">
				<div class="search-bar-result search-result no-result">
					<div class="no-result-headline">Nessun risultato trovato.</div>
					<div class="no-result-text">Prova a cercare una città, un codice postale o un punto di interesse.</div>
				</div>
			</div>
		</div>
	</div>
</div>

					
					<a href="/it/videos" class="video-wall-icon">
						<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><path fill-rule="evenodd" clip-rule="evenodd" d="M17.0946 14.2044H0.75V1.5H17.0946V14.2044ZM16.2751 13.3847H1.56964V2.31948H16.2751V13.3847ZM7.4518 5.42938V10.2508L11.1643 7.8401L7.4518 5.42938ZM6.63216 3.91071L12.2491 7.55081V8.10528L6.63216 11.7696V3.91071Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4.82422 16.5884H13.0207V15.7687H4.82422V16.5884Z" fill="white"></path></svg>
					</a>
					
				
				<svg class="hamburger-button icon-hamburger" data-qa="navigationMenu" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
                <defs>
                    <path id="svghamburger" d="M10 12v1H0v-1h10zm6-6v1H0V6h16zm0-6v1H0V0h16z"></path>
                </defs>
                <use fill="#FFF" fill-rule="evenodd" transform="matrix(-1 0 0 1 20 6)" xlink:href="#svghamburger"></use></svg>
				<svg class="close-button close-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><g fill-rule="evenodd" transform="translate(-1 -1)"><rect width="2" height="24" x="9" y="-2" rx="1" transform="rotate(45 10 10)"></rect><rect width="2" height="24" x="9" y="-2" rx="1" transform="rotate(-45 10 10)"></rect></g></svg>
			</div>
		</div>
	</div>

	<div class="header-menu">
		
		<div class="settings-link">
			<a href="/it/settings">
				<svg class="icon-settings" xmlns="http://www.w3.org/2000/svg" width="24" height="25" viewBox="0 0 24 25" fill="#FFF"><path d="M13.677.107l.871 2.674c.775.225 1.549.483 2.162.902l2.58-1.32 2.452 2.447-1.29 2.578c.354.612.645 1.353.87 2.094l2.678.902v3.414l-2.645.838c-.258.773-.549 1.578-.903 2.255l1.29 2.48-2.452 2.449-2.58-1.224c-.645.386-1.387.676-2.162.902l-.87 2.609h-3.42l-.903-2.61c-.742-.225-1.484-.482-2.161-.934L4.742 21.82 2.29 19.372l1.29-2.449c-.386-.676-.677-1.45-.903-2.255L0 13.798v-3.447l2.71-.902c.193-.74.451-1.481.87-2.094L2.29 4.843l2.452-2.449 2.452 1.289c.677-.387 1.419-.677 2.16-.902l.904-2.674h3.42zm-.838 1.128h-1.807l-.806 2.448-.549.193c-.677.194-1.354.419-1.935.773l-.548.29-2.29-1.16L3.58 5.1l1.225 2.384-.354.548c-.323.483-.581 1.127-.71 1.74l-.13.612-2.515.805v1.804l2.451.805.194.58c.193.677.42 1.385.774 1.965l.29.548-1.16 2.287L4.967 20.5l2.322-1.16.549.355c.58.354 1.226.612 1.903.773l.548.193.775 2.32h1.838l.774-2.417.581-.128c.677-.194 1.323-.42 1.903-.741l.484-.322 2.42 1.127 1.322-1.32-1.161-2.288.29-.483c.323-.645.58-1.353.774-2.062l.194-.58 2.42-.74V11.19l-2.452-.805-.194-.548c-.193-.677-.42-1.32-.742-1.836l-.29-.548 1.161-2.384-1.322-1.353-2.388 1.256-.548-.354a7.5 7.5 0 00-1.903-.74l-.58-.194-.807-2.448zm-.871 5.38c3.032 0 5.548 2.448 5.548 5.508 0 3.028-2.516 5.541-5.548 5.541-3.065 0-5.516-2.545-5.516-5.54a5.49 5.49 0 015.516-5.51zm0 1.063c-2.323 0-4.355 2.093-4.355 4.445 0 2.352 2.032 4.446 4.355 4.446 2.322 0 4.387-2.126 4.387-4.446 0-2.352-2.065-4.445-4.387-4.445z"></path></svg>
				impostazioni
			</a>
			
			
				<svg class="close-button desktop-close close-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><g fill-rule="evenodd" transform="translate(-1 -1)"><rect width="2" height="24" x="9" y="-2" rx="1" transform="rotate(45 10 10)"></rect><rect width="2" height="24" x="9" y="-2" rx="1" transform="rotate(-45 10 10)"></rect></g></svg>
			
		</div>
		<a class="header-link" target="_blank" href="https://support.accuweather.com/faq/">
			Guida
		</a>
		<div class="header-loc-weather">Meteo di Roma, Lazio</div>
			<a data-page-id="three-day" data-ga-page-id="today" class="header-link active" href="/it/it/rome/213490/weather-forecast/213490">Oggi</a>
			<a data-page-id="wintercast" data-ga-page-id="wintercast" class="header-link nav-red-dot hidden winter-link " href="/it/it/rome/213490/winter-weather-forecast/213490">WinterCast</a>
			<a data-page-id="tropical" data-ga-page-id="local_{stormName}_tracker" class="header-link nav-red-tropical-image northern side-item hidden tropical-link " href="/it/it/rome/213490/tropical-weather-forecast/213490?eventkey={eventkey}">Tracciamento locale di {stormName}</a>
			<a data-page-id="hourly" data-ga-page-id="hourly" class="header-link " href="/it/it/rome/213490/hourly-weather-forecast/213490">Orario</a>
			<a data-page-id="daily" data-ga-page-id="daily" class="header-link " href="/it/it/rome/213490/10-day-weather-forecast/213490">10 giorni</a>
			<a data-page-id="city-radar" data-ga-page-id="radar" class="header-link " href="/it/it/rome/213490/weather-radar/213490">Radar</a>
			<a data-page-id="minutecast" data-ga-page-id="minutecast" class="header-link " href="/it/it/rome/213490/minute-weather-forecast/213490">MinuteCast®</a>
			<a data-page-id="monthly" data-ga-page-id="monthly" class="header-link " href="/it/it/rome/213490/april-weather/213490">Mensile</a>
			<a data-page-id="air-quality" data-ga-page-id="air_quality" class="header-link " href="/it/it/rome/213490/air-quality-index/213490">Qualità dell'aria</a>
			<a data-page-id="lifestyle-home" data-ga-page-id="health_and_activities" class="header-link " href="/it/it/rome/213490/health-activities/213490">Salute e attività</a>
		
<div class="more-cta-links ">
	<h2 class="more-cta-title">
		<p>Intorno al mondo</p>
	</h2>
			<a href="/it/hurricane" class="cta-link" data-page-id="hurricane" data-ga-page-id="hurricane_tracker">
				<h3 class="cta-text">Uragano</h3>
				<svg class="icon-arrow" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><defs><path id="a" d="m8.495.505 5 5v.99l-5 5-.99-.99 3.805-3.806L0 6.7V5.3l11.31-.001-3.805-3.804.99-.99z"></path></defs><use fill="#000" fill-rule="nonzero" xlink:href="#a" transform="translate(2 3)"></use></svg>
			</a>
			<a href="/it/it/severe-weather" class="cta-link" data-page-id="severe-weather" data-ga-page-id="severe_weather">
				<h3 class="cta-text">Clima avverso</h3>
				<svg class="icon-arrow" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><defs><path id="a" d="m8.495.505 5 5v.99l-5 5-.99-.99 3.805-3.806L0 6.7V5.3l11.31-.001-3.805-3.804.99-.99z"></path></defs><use fill="#000" fill-rule="nonzero" xlink:href="#a" transform="translate(2 3)"></use></svg>
			</a>
			<a href="/it/it/lazio/weather-radar" class="cta-link" data-page-id="map-radar" data-ga-page-id="radar_and_maps">
				<h3 class="cta-text">Radar e mappe</h3>
				<svg class="icon-arrow" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><defs><path id="a" d="m8.495.505 5 5v.99l-5 5-.99-.99 3.805-3.806L0 6.7V5.3l11.31-.001-3.805-3.804.99-.99z"></path></defs><use fill="#000" fill-rule="nonzero" xlink:href="#a" transform="translate(2 3)"></use></svg>
			</a>
			<a href="/it/videos" class="cta-link" data-page-id="video-wall" data-ga-page-id="video">
				<h3 class="cta-text">Video</h3>
				<svg class="icon-arrow" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><defs><path id="a" d="m8.495.505 5 5v.99l-5 5-.99-.99 3.805-3.806L0 6.7V5.3l11.31-.001-3.805-3.804.99-.99z"></path></defs><use fill="#000" fill-rule="nonzero" xlink:href="#a" transform="translate(2 3)"></use></svg>
			</a>
</div>

	</div>
</div>
<div class="header-placeholder   "></div>

	<div class="page-subnav">
		
	<div class="subnav secondary-nav" data-gatype="city">
	<div class="overflow overflow-left" data-qa="leftArrow">
		<svg class="arrow chevron-icon left" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
	</div>
	<div class="overflow overflow-right" data-qa="rightArrow">
		<svg class="arrow chevron-icon right" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
	</div>
	<div class="subnav-items">
				<a class="subnav-item active" href="/it/it/rome/213490/weather-forecast/213490" data-qa="now" data-gaid="now" data-pageid="three-day">
						<h2>Oggi</h2>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/hourly-weather-forecast/213490" data-qa="hourly" data-gaid="hourly" data-pageid="hourly">
						<span>Orario</span>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/10-day-weather-forecast/213490" data-qa="daily" data-gaid="daily" data-pageid="daily">
						<span>10 giorni</span>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/weather-radar/213490" data-qa="radar" data-gaid="radar" data-pageid="city-radar">
						<span>Radar</span>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/minute-weather-forecast/213490" data-qa="minutecast" data-gaid="minutecast" data-pageid="minutecast">
						<span>MinuteCast®</span>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/april-weather/213490" data-qa="monthly" data-gaid="monthly" data-pageid="monthly">
						<span>Mensile</span>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/air-quality-index/213490" data-qa="airQuality" data-gaid="airQuality" data-pageid="air-quality">
						<span>Qualità dell'aria</span>
				</a>
				<a class="subnav-item " href="/it/it/rome/213490/health-activities/213490" data-qa="lifestyles" data-gaid="lifestyles" data-pageid="lifestyle-home">
						<span>Salute e attività</span>
				</a>
		<div class="subnav-item filler"></div>
	</div>
</div>





	</div>
	
		<div class="glacier-ad unrendered top config-top content-module" ad-type="top" id="top" data-google-query-id="CP6nya6V_JMDFRBCkQQdA2cIbA"><div id="google_ads_iframe_/6581/web/it/top/weather/local_home_0__container__" style="border: 0pt; margin: auto; text-align: center;"><iframe id="google_ads_iframe_/6581/web/it/top/weather/local_home_0" name="google_ads_iframe_/6581/web/it/top/weather/local_home_0" title="Contenuto dell'annuncio di terze parti" width="970" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Pubblicità" tabindex="0" data-load-complete="true" data-google-container-id="1" style="border: 0px; vertical-align: bottom;"></iframe></div></div>

	
	
		<div class="glacier-ad unrendered oop config-oop " ad-type="oop" id="oop" data-google-query-id="CPOYyK6V_JMDFZI-VQgd8_oh1w"><div id="google_ads_iframe_/6581/web/it/oop/weather/local_home_0__container__" style="border: 0pt; margin: auto; text-align: center;"></div></div>

		<div class="glacier-ad unrendered interstitial config-interstitial " ad-type="interstitial" id="interstitial"></div>

	
	<div class="two-column-page-content ">
		<div class="page-column-1">
			<div class="page-content content-module">
				
					<a href="/it/it/rome/213490/weather-warnings/213490" class="severe-alert-banner content-module lbar-banner">
	<svg class="severe-alert-banner__icon  alert-icon" xmlns="http://www.w3.org/2000/svg" width="25" height="22" viewBox="0 0 25 22"><path fill="#fff" d="M13.273.438L24.87 19.766c.36.6-.072 1.366-.773 1.366H.903c-.7 0-1.134-.765-.773-1.366L11.727.438c.35-.584 1.196-.584 1.546 0zm.129 14.638h-1.804v2.577h1.804v-2.577zm0-7.731h-1.804v6.442h1.804V7.345z" transform="translate(0 -8) translate(0 8)"></path></svg>
	<span class="severe-alert-banner__count">2</span>
	<div class="severe-alert-banner__separator"></div>
	<span class="severe-alert-banner__type">Allarme giallo per temporali</span>
	<svg class="icon-arrow" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><defs><path id="a" d="m8.495.505 5 5v.99l-5 5-.99-.99 3.805-3.806L0 6.7V5.3l11.31-.001-3.805-3.804.99-.99z"></path></defs><use fill="#000" fill-rule="nonzero" xlink:href="#a" transform="translate(2 3)"></use></svg>
</a>

				
				

	

	<a class="cur-con-weather-card is-desktop lbar-panel content-module " href="/it/it/rome/213490/current-weather/213490">
	<div class="title-container">
		<h2 class="cur-con-weather-card__title">
			Meteo attuale
		</h2>
		<p class="cur-con-weather-card__subtitle">
			11:57
		</p>
	</div>
	<div class="cur-con-weather-card__body">
		<div class="cur-con-weather-card__panel">
			<div class="forecast-container">
				<img class="weather-icon" src="/images/weathericons/v2a/03.svg" width="88" height="88">
				<div class="temp-container">
					<div class="temp">21°<span class="after-temp">C</span></div>
					<div class="real-feel">
						RealFeel®
						24°
					</div>
				</div>
			</div>
			<div>
				<span class="phrase">Parzialmente soleggiato</span>
				<span class="cur-con-weather-card__cta">
					<span class="text">Altri dettagli</span>
					<svg class="icon-chevron chevron-icon right" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
				</span>
			</div>
		</div>
		<div class="cur-con-weather-card__panel details-container">
			<div class="spaced-content detail">
				<span class="label">RealFeel Shade™</span>
				<span class="value">19°</span>
			</div>
			<div class="spaced-content detail">
				<span class="label">Vento</span>
				<span class="value">ESE 12 km/h</span>
			</div>
			<div class="spaced-content detail">
				<span class="label">Raffiche vento</span>
				<span class="value">25 km/h</span>
			</div>
			<div class="spaced-content detail">
				<span class="label">Qualità dell'aria</span>
				<span class="value" style="color: #FDB80D">Sfavorev.</span>
			</div>
		</div>
	</div>
</a>


	

	
		
<a class="local-forecast-summary" href="/it/it/rome/213490/daily-weather-forecast/213490?day=3">
	<h2>Evoluzione</h2>
	<p>Sono previsti rovesci mercoledì pomeriggio</p>
</a>

	

	
	

	
<div class="recommended-map-container  " data-title="Roma - Radar meteo">
	<h2 class="title">Roma - Radar meteo</h2>
	

<a class="base-map-cta card static-radar-map-recommended " href="/it/it/rome/213490/weather-radar/213490" data-title="Roma - Radar meteo">
	
	
	<img alt="Roma - Radar meteo" class="component-image responsive-img lazy" data-src="https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&amp;zoom=3&amp;lon=12.833&amp;lat=42.833&amp;imgwidth=768&amp;imgheight=432&amp;language=it&amp;base_data=radar" data-srcset="https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&amp;zoom=3&amp;lon=12.833&amp;lat=42.833&amp;imgwidth=768&amp;imgheight=432&amp;language=it&amp;base_data=radar, https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&amp;zoom=4&amp;lon=12.833&amp;lat=42.833&amp;imgwidth=480&amp;imgheight=270&amp;language=it&amp;base_data=radar" sizes="" src="https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&amp;zoom=3&amp;lon=12.833&amp;lat=42.833&amp;imgwidth=768&amp;imgheight=432&amp;language=it&amp;base_data=radar" title="Roma - Radar meteo" srcset="https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&amp;zoom=3&amp;lon=12.833&amp;lat=42.833&amp;imgwidth=768&amp;imgheight=432&amp;language=it&amp;base_data=radar, https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&amp;zoom=4&amp;lon=12.833&amp;lat=42.833&amp;imgwidth=480&amp;imgheight=270&amp;language=it&amp;base_data=radar">

	
<div class="  map-error-message">
	<div class="map-error-message-content">
		<div class="error-heading"><span id="mapName">Static Radar</span> Temporarily Unavailable</div>
		<div class="error-thanks">Thank you for your patience as we work to get everything up and running again.</div>
		<div class="error-refresh" onclick="javascript: location.reload()">Refresh Page</div>
	</div>
</div>

	
</a>

	<div class="cta-container">
		
<div class="recommended-maps">
	<a href="/it/it/rome/213490/satellite/213490">	
		<div class="recommended-maps__item">
			<img src="https://www.awxcdn.com/adc-assets/images/components/maps/mapping-layers/realvue-satellite.jpg" height="40" width="40" class="recommended-maps__item-image">
			<span class="recommended-maps__item-name">Nuvole</span>
		</div>
	</a>
	<a href="/it/it/lazio/current-weather-maps">	
		<div class="recommended-maps__item">
			<img src="https://www.awxcdn.com/adc-assets/images/components/maps/mapping-layers/temperature.jpg" height="40" width="40" class="recommended-maps__item-image">
			<span class="recommended-maps__item-name">Temperatura</span>
		</div>
	</a>
</div>

	</div>
</div>


	<div class="hourly-list-wrapper content-module">
	<h2 class="hourly-list-header">Previsioni orarie</h2>
	<div class="hourly-list has-arrow-right">
		<button class="hourly-list__arrow hourly-list__arrow-left hide">
			<svg class="icon-chevron left arrow" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6" role="img" aria-labelledby="chevronSVG">
	<title id="chevronSVG">Chevron left</title>
	<path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path>
</svg>

		</button>
		<div class="hourly-list__list-wrapper">
			<div class="hourly-list__list" style="transform: translateX(4px);">
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776679200">
						<span class="hourly-list__list__item-time">
12						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
						<span class="hourly-list__list__item-temp">21°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>2%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776682800">
						<span class="hourly-list__list__item-time">
13						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
						<span class="hourly-list__list__item-temp">22°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>1%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776686400">
						<span class="hourly-list__list__item-time">
14						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/1.svg">
						<span class="hourly-list__list__item-temp">23°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>0%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776690000">
						<span class="hourly-list__list__item-time">
15						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/1.svg">
						<span class="hourly-list__list__item-temp">23°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>0%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776693600">
						<span class="hourly-list__list__item-time">
16						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/1.svg">
						<span class="hourly-list__list__item-temp">22°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>0%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776697200">
						<span class="hourly-list__list__item-time">
17						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
						<span class="hourly-list__list__item-temp">22°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>0%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776700800">
						<span class="hourly-list__list__item-time">
18						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
						<span class="hourly-list__list__item-temp">21°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>0%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776704400">
						<span class="hourly-list__list__item-time">
19						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
						<span class="hourly-list__list__item-temp">20°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>0%</span>
						</div>
					</a>
					<a class="hourly-list__list__item" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776708000">
						<span class="hourly-list__list__item-time">
20						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/34.svg">
						<span class="hourly-list__list__item-temp">19°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg" src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>1%</span>
						</div>
					</a>
					<a class="hourly-list__list__item hide" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776711600">
						<span class="hourly-list__list__item-time">
21						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/34.svg">
						<span class="hourly-list__list__item-temp">17°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>1%</span>
						</div>
					</a>
					<a class="hourly-list__list__item hide" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776715200">
						<span class="hourly-list__list__item-time">
22						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/35.svg">
						<span class="hourly-list__list__item-temp">16°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>1%</span>
						</div>
					</a>
					<a class="hourly-list__list__item hide" href="/it/it/rome/213490/hourly-weather-forecast/213490?hour=1776718800">
						<span class="hourly-list__list__item-time">
23						</span>
						<img class="hourly-list__list__item-icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/35.svg">
						<span class="hourly-list__list__item-temp">16°</span>
						<div class="hourly-list__list__item-precip">
							<img alt="rain drop" class="precip-icon" data-src="https://www.awxcdn.com/adc-assets/images/components/weather/hourly-card-nfl/drop-icon.svg">
							<span>1%</span>
						</div>
					</a>
			</div>
		</div>
		<button class="hourly-list__arrow hourly-list__arrow-right">
			<svg class="icon-chevron right arrow" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6" role="img" aria-labelledby="chevronSVG">
	<title id="chevronSVG">Chevron right</title>
	<path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path>
</svg>

		</button>
	</div>
</div>


	
<div class="daily-list content-module">
	<h2 class="daily-list-header">Previsioni giorno</h2>
	<div class="daily-list-body">
			<a class="daily-list-item " href="/it/it/rome/213490/weather-today/213490">
				<div class="date" style="width: 45px;">
					<p class="day">Oggi</p>
					<p>20/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">23°</span>
						<span class="temp-lo">12°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Da soleggiato a parzialmente nuvoloso</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/35.svg">
						<p class="no-wrap">Parzialmente nuvoloso</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					12%
				</div>
			</a>
			<a class="daily-list-item has-alerts" href="/it/it/rome/213490/weather-tomorrow/213490">
				<div class="date" style="width: 45px;">
					<p class="day">mar</p>
					<p>21/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/3.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">23°</span>
						<span class="temp-lo">12°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Sole con qualche nuvola</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/35.svg">
						<p class="no-wrap">Parzialmente nuvoloso</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					9%
				</div>
			</a>
			<a class="daily-list-item has-alerts" href="/it/it/rome/213490/daily-weather-forecast/213490?day=3">
				<div class="date" style="width: 45px;">
					<p class="day">mer</p>
					<p>22/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/14.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">20°</span>
						<span class="temp-lo">9°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Uno o due brevi rovesci</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/35.svg">
						<p class="no-wrap">Parzialmente nuvoloso</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					63%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=4">
				<div class="date" style="width: 45px;">
					<p class="day">gio</p>
					<p>23/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/1.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">21°</span>
						<span class="temp-lo">6°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Ampiamente soleggiato</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/33.svg">
						<p class="no-wrap">Sereno</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					0%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=5">
				<div class="date" style="width: 45px;">
					<p class="day">ven</p>
					<p>24/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/1.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">23°</span>
						<span class="temp-lo">8°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Ampiamente soleggiato</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/34.svg">
						<p class="no-wrap">Prevalentemente sereno</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					0%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=6">
				<div class="date" style="width: 45px;">
					<p class="day">sab</p>
					<p>25/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/3.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">23°</span>
						<span class="temp-lo">10°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Parzialmente soleggiato</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/33.svg">
						<p class="no-wrap">Sereno</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					0%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=7">
				<div class="date" style="width: 45px;">
					<p class="day">dom</p>
					<p>26/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/2.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">22°</span>
						<span class="temp-lo">11°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Prevalentemente soleggiato</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/35.svg">
						<p class="no-wrap">Parzialmente nuvoloso</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					0%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=8">
				<div class="date" style="width: 45px;">
					<p class="day">lun</p>
					<p>27/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/6.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">22°</span>
						<span class="temp-lo">11°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Prevalentemente nuvoloso</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/7.svg">
						<p class="no-wrap">Nuvoloso</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					4%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=9">
				<div class="date" style="width: 45px;">
					<p class="day">mar</p>
					<p>28/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/7.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">22°</span>
						<span class="temp-lo">12°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Nuvoloso</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/38.svg">
						<p class="no-wrap">Prevalentemente nuvoloso</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					25%
				</div>
			</a>
			<a class="daily-list-item " href="/it/it/rome/213490/daily-weather-forecast/213490?day=10">
				<div class="date" style="width: 45px;">
					<p class="day">mer</p>
					<p>29/4</p>
				</div>
				<img class="icon" height="40" width="40" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/4.svg">
				<div class="temp-phrase-wrapper">
					<div class="temp">
						<span class="temp-hi">23°</span>
						<span class="temp-lo">12°</span>
					</div>
				</div>
				<div class="phrase">
					<p class="no-wrap">Nuvole e sole</p>
					<span class="night">
						<img class="night-icon" height="22" width="22" src="https://www.awxcdn.com/adc-assets/images/weathericons/v2a/33.svg">
						<p class="no-wrap">Sereno</p>
					</span>
				</div>

				<div class="precip">
					<svg class="precip-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 16"><path fill="none" fill-rule="nonzero" stroke="#000" stroke-width=".714" d="M5.532.891c1.723.952 5.315 5.477 5.775 8.756.028 1.718-.534 3.101-1.45 4.082C8.888 14.766 7.52 15.357 6 15.357a5.532 5.532 0 0 1-3.74-1.425c-.975-.89-1.587-2.124-1.616-3.49.503-4.035 4.013-8.49 4.888-9.551Zm-1.815 7.33a.336.336 0 0 0-.025.043c-.322.62-.59 1.255-.695 2.207.012.408.143.787.358 1.111.234.352.568.641.96.839.035.017.071.021.106.017a.201.201 0 0 0 .104-.044l.01-.005-.078-.1c-.328-.415-.82-1.067-.82-1.946 0-.752.076-1.613.08-2.121Z"></path></svg>
					19%
				</div>
			</a>
	</div>
</div>


	<div class="sunrise-sunset content-module ">
	<h2 class="sunrise-sunset__title">
		Sole e luna
	</h2>
	<div class="sunrise-sunset__body">
			<div class="sunrise-sunset__item">
				<img class="sunrise-sunset__icon sun-icon" width="40" height="40" aria-hidden="true" src="/images/weathericons/v2a/1.svg">
				<span class="sunrise-sunset__phrase">13 h 33 min</span>
				<div class="sunrise-sunset__times">
					<div class="sunrise-sunset__times-item">
						<span class="sunrise-sunset__times-label">Alba</span>
						<span class="sunrise-sunset__times-value">06:23</span>
					</div>
					<div class="sunrise-sunset__times-item">
						<span class="sunrise-sunset__times-label">Tramontare</span>
						<span class="sunrise-sunset__times-value">19:56</span>
					</div>
				</div>
			</div>
			<div class="sunrise-sunset__item">
				<img class="sunrise-sunset__icon" width="40" height="40" aria-hidden="true" src="/images/moon-phases/colored/light/WaxingCrescent.svg">
				<span class="sunrise-sunset__phrase">16 h 22 min</span>
				<div class="sunrise-sunset__times">
					<div class="sunrise-sunset__times-item">
						<span class="sunrise-sunset__times-label">Alba</span>
						<span class="sunrise-sunset__times-value">07:53</span>
					</div>
					<div class="sunrise-sunset__times-item">
						<span class="sunrise-sunset__times-label">Tramontare</span>
						<span class="sunrise-sunset__times-value">00:15</span>
					</div>
				</div>
			</div>
	</div>
</div>


	<script>
	window.collapseConnatix = () => {
		const connatixEl = document.getElementById('connatix');
		if (connatixEl) {
			connatixEl.style.display = "none";
		}
	}
</script>



	

	<a href="/it/it/rome/213490/air-quality-index/213490" class="air-quality-module-wrapper">

	<div class="air-quality-module__title">
		<h2>Qualità dell'aria</h2>
		<span>Visualizza altro</span>
	</div>
	<div class="air-quality-module content-module">
		<div class="air-quality-module__row">
			<span class="air-quality-module__row__1">
				<svg class="air-quality-module__icon" width="24" height="25" viewBox="5 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
					<g clip-path="url(#clip0_4782_28057)">
						<path d="M6.75 6.16675C6.75 4.92411 7.75736 3.91675 9 3.91675H15C16.2426 3.91675 17.25 4.92411 17.25 6.16675V18.1667C17.25 19.4094 16.2426 20.4167 15 20.4167H9C7.75736 20.4167 6.75 19.4094 6.75 18.1667V6.16675Z" stroke="black" stroke-width="1.5"></path>
						<path d="M11.25 8.41675L12.8991 7.53828C14.4959 6.68762 16.4223 6.73896 17.9716 7.67344V7.67344C19.5089 8.6007 21.4185 8.65888 23.0094 7.82695L24.75 6.91675" stroke="black" stroke-width="1.5"></path>
						<path d="M11.25 12.9167L12.8991 12.0383C14.4959 11.1876 16.4223 11.239 17.9716 12.1734V12.1734C19.5089 13.1007 21.4185 13.1589 23.0094 12.3269L24.75 11.4167" stroke="black" stroke-width="1.5"></path>
						<path d="M11.25 17.4167L12.8991 16.5383C14.4959 15.6876 16.4223 15.739 17.9716 16.6734V16.6734C19.5089 17.6007 21.4185 17.6589 23.0094 16.8269L24.75 15.9167" stroke="black" stroke-width="1.5"></path>
					</g>
					<defs>
						<clipPath id="clip0_4782_28057">
							<rect width="24" height="24" fill="white" transform="translate(0 0.166748)"></rect>
						</clipPath>
					</defs>
				</svg>
				<span>Qualità dell'aria</span>
			</span>
			<span class="air-quality-module__row__category" style="border-color: #FDB80D;">Sfavorev.</span>
		</div>
		<p class="air-quality-module__statement">
			L'aria ha raggiunto un livello elevato di inquinamento ed è malsana per i gruppi sensibili. Riduci il tempo trascorso all'aperto se hai sintomi quali difficoltà respiratoria o irritazione della gola.
		</p>
		
	</div>

	</a>



	


<div class="health-activities__title">
	<h2>
		Situazione allergie
	</h2>
	<a href="/it/it/rome/213490/health-activities/213490">Vedi tutto</a>
</div>

<div class="health-activities  health-activities-free">
		<a data-slug="tree-pollen" href="/it/it/rome/213490/allergies-weather/213490?name=tree-pollen" class="health-activities__item show " style="border-right-color: #93c701;">
			<svg class="health-activities__item__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12.4257 2H11.5175L2.89999 18.6196L3.34399 19.3562H8.3894V18.3471H4.16135L11.9817 3.33199L19.8425 18.3471H15.3117V19.3562H20.6699L21.124 18.6095L12.4257 2Z" fill="black"></path><path d="M15.2814 14.3209L12.3651 17.4188V22H11.3561V16.1675L8.73245 13.3824L9.46908 12.6862L11.3561 14.6943V9.6993H12.3651V12.3532L14.0099 10.6176L14.7365 11.3138L12.3651 13.8264V15.9455L14.5347 13.6347L15.2814 14.3209Z" fill="black"></path></svg></svg>
			<span class="health-activities__item__name">Polline di albero</span>
			<span class="health-activities__item__category" style="border-right: 3px solid #93c701">Bassa</span>
			<span class="health-activities__item__category__unsupported" style="border-right: 3px solid transparent">Dati non supportati in questa posizione</span>
		</a>
		<a data-slug="ragweed-pollen" href="/it/it/rome/213490/allergies-weather/213490?name=ragweed-pollen" class="health-activities__item show " style="border-right-color: #93c701;">
			<svg class="health-activities__item__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.76971 15.58C7.67593 15.58 5.87549 14.56 5.05618 14C3.18494 12.74 1.95092 11.04 2.0015 9.77L2.02173 9.37L2.41621 9.3C9.4258 7.99 12.3996 14.37 12.4299 14.43L12.6423 14.89L12.177 15.09C11.3577 15.44 10.5486 15.58 9.77982 15.58H9.76971ZM3.06356 10.2C3.27597 11 4.15596 12.19 5.62262 13.17C7.49387 14.43 9.5573 14.86 11.2465 14.35C10.4777 13.03 7.95915 9.52 3.06356 10.19V10.2Z" fill="black"></path><path d="M21.9783 9.2L21.5839 9.13C17.8312 8.41 15.3025 9.74 13.7246 11.25L14.4124 11.93C15.7476 10.68 17.8414 9.58 20.9466 10.04C20.7342 11.05 19.6721 12.38 18.2763 13.31C17.3761 13.91 15.1103 15.15 12.6423 14.32L11.9039 13.59C11.6308 14.08 11.4993 14.41 11.4892 14.42L11.3274 14.86L11.7623 15.05C12.5816 15.41 13.4616 15.59 14.3618 15.59C15.8588 15.59 17.4064 15.1 18.8427 14.14C20.7544 12.87 22.0491 11 21.9986 9.6L21.9783 9.2Z" fill="black"></path><path d="M12.4704 14.47H11.4589V22H12.4704V14.47Z" fill="black"></path><path d="M11.115 7.48C11.115 7.91 11.469 8.26 11.9039 8.26C12.3389 8.26 12.6929 7.91 12.6929 7.48C12.6929 7.05 12.3389 6.7 11.9039 6.7C11.469 6.7 11.115 7.05 11.115 7.48Z" fill="black"></path><path d="M13.492 5.13C13.492 5.56 13.846 5.91 14.2809 5.91C14.7159 5.91 15.0699 5.56 15.0699 5.13C15.0699 4.7 14.7159 4.35 14.2809 4.35C13.846 4.35 13.492 4.7 13.492 5.13Z" fill="black"></path><path d="M8.73798 5.13C8.73798 5.56 9.092 5.91 9.52694 5.91C9.96187 5.91 10.3159 5.56 10.3159 5.13C10.3159 4.7 9.96187 4.35 9.52694 4.35C9.092 4.35 8.73798 4.7 8.73798 5.13Z" fill="black"></path><path d="M15.869 2.78C15.869 3.21 16.223 3.56 16.6579 3.56C17.0929 3.56 17.4469 3.21 17.4469 2.78C17.4469 2.35 17.0929 2 16.6579 2C16.223 2 15.869 2.35 15.869 2.78Z" fill="black"></path><path d="M6.36099 2.78C6.36099 3.21 6.71501 3.56 7.14995 3.56C7.58489 3.56 7.93891 3.21 7.93891 2.78C7.93891 2.35 7.59501 2 7.14995 2C6.7049 2 6.36099 2.35 6.36099 2.78Z" fill="black"></path><path d="M11.115 2.78C11.115 3.21 11.469 3.56 11.9039 3.56C12.3389 3.56 12.6929 3.21 12.6929 2.78C12.6929 2.35 12.3389 2 11.9039 2C11.469 2 11.115 2.35 11.115 2.78Z" fill="black"></path><path d="M12.4701 14.92V14.97L12.4501 14.92H12.4701Z" fill="black"></path></svg></svg>
			<span class="health-activities__item__name">Polline di ambrosia</span>
			<span class="health-activities__item__category" style="border-right: 3px solid #93c701">Bassa</span>
			<span class="health-activities__item__category__unsupported" style="border-right: 3px solid transparent">Dati non supportati in questa posizione</span>
		</a>
		<a data-slug="mold" href="/it/it/rome/213490/allergies-weather/213490?name=mold" class="health-activities__item show " style="border-right-color: #f05514;">
			<svg class="health-activities__item__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M22.2912 13.4197V12.4108H20.8975C20.8559 11.7764 20.7415 11.1524 20.5543 10.5699L21.7088 10.0811L21.324 9.15549L20.1799 9.63391C19.8783 9.00988 19.5039 8.42746 19.0567 7.90744L20.0343 6.9194L19.3271 6.20177L18.339 7.17941C17.8294 6.71139 17.2366 6.32657 16.6022 6.01456L17.0598 4.90172L16.1342 4.5169L15.6765 5.61935C15.0525 5.41134 14.3869 5.27613 13.7109 5.23453V3.84087H12.702V5.23453C11.9636 5.27613 11.2564 5.42174 10.5907 5.67135L10.1019 4.5273L9.17628 4.91212L9.66509 6.07696C9.36348 6.24337 9.07227 6.40978 8.80186 6.60738L9.52989 7.31461C10.5907 6.61779 11.8492 6.21217 13.2116 6.21217C16.9038 6.21217 19.9199 9.21789 19.9199 12.9204C19.9199 15.6141 18.3182 18.027 15.8325 19.0879L15.7909 19.1087C14.9797 19.4519 14.1061 19.6183 13.2116 19.6183C9.50909 19.6183 6.49297 16.6126 6.49297 12.91C6.49297 11.6412 6.85698 10.4555 7.48101 9.4363L6.73218 8.71867C6.54497 9.03068 6.35776 9.34269 6.21216 9.67551L4.9329 9.15549L4.54809 10.0811L5.83774 10.6115C5.66093 11.1836 5.55693 11.7868 5.51533 12.4108H4.13207V13.4197H5.51533C5.56733 14.1581 5.71294 14.8549 5.95215 15.5205L4.54809 16.103L4.9329 17.0286L6.35776 16.4462C6.65937 17.0286 7.04419 17.5798 7.48101 18.0582L6.50337 19.0359L7.221 19.7535L8.19864 18.7655C8.68746 19.1815 9.22828 19.5455 9.8003 19.8263L9.19708 21.2928L10.1227 21.6776L10.7259 20.2215C11.3604 20.4295 12.0156 20.5647 12.7124 20.6167V22H13.7213V20.6167C14.3453 20.5751 14.9589 20.4607 15.5517 20.2735L16.1342 21.6776L17.0598 21.2928L16.4878 19.8887C17.143 19.5767 17.7462 19.1815 18.287 18.7239L19.3375 19.7639L20.0447 19.0463L19.0151 18.0062C19.4103 17.5486 19.7535 17.039 20.0343 16.5086L21.324 17.039L21.7088 16.1134L20.4399 15.5829C20.6895 14.9069 20.8455 14.1789 20.8975 13.4405H22.3016L22.2912 13.4197Z" fill="black"></path><path d="M13.2116 12.0572C12.7332 12.0572 12.3588 12.442 12.3588 12.91C12.3588 13.3781 12.7436 13.7629 13.2116 13.7629C13.6797 13.7629 14.0645 13.3781 14.0645 12.91C14.0645 12.442 13.6797 12.0572 13.2116 12.0572Z" fill="black"></path><path d="M9.7795 10.3411C10.2505 10.3411 10.6323 9.95931 10.6323 9.4883C10.6323 9.01729 10.2505 8.63547 9.7795 8.63547C9.30849 8.63547 8.92667 9.01729 8.92667 9.4883C8.92667 9.95931 9.30849 10.3411 9.7795 10.3411Z" fill="black"></path><path d="M9.7795 15.4893C9.30108 15.4893 8.92667 15.8742 8.92667 16.3422C8.92667 16.8102 9.31148 17.195 9.7795 17.195C10.2475 17.195 10.6323 16.8102 10.6323 16.3422C10.6323 15.8742 10.2475 15.4893 9.7795 15.4893Z" fill="black"></path><path d="M16.6438 10.3411C17.1148 10.3411 17.4966 9.95931 17.4966 9.4883C17.4966 9.01729 17.1148 8.63547 16.6438 8.63547C16.1728 8.63547 15.7909 9.01729 15.7909 9.4883C15.7909 9.95931 16.1728 10.3411 16.6438 10.3411Z" fill="black"></path><path d="M16.6438 15.4893C16.1758 15.4893 15.7909 15.8742 15.7909 16.3422C15.7909 16.8102 16.1758 17.195 16.6438 17.195C17.1118 17.195 17.4966 16.8102 17.4966 16.3422C17.4966 15.8742 17.1118 15.4893 16.6438 15.4893Z" fill="black"></path><path d="M13.2116 18.9111C13.6827 18.9111 14.0645 18.5293 14.0645 18.0582C14.0645 17.5872 13.6827 17.2054 13.2116 17.2054C12.7406 17.2054 12.3588 17.5872 12.3588 18.0582C12.3588 18.5293 12.7406 18.9111 13.2116 18.9111Z" fill="black"></path><path d="M13.2116 6.9194C12.7332 6.9194 12.3588 7.30421 12.3588 7.77223C12.3588 8.24025 12.7436 8.62506 13.2116 8.62506C13.6797 8.62506 14.0645 8.24025 14.0645 7.77223C14.0645 7.30421 13.6797 6.9194 13.2116 6.9194Z" fill="black"></path><path d="M19.2127 12.91C19.2127 12.4316 18.8279 12.0572 18.3598 12.0572C17.8918 12.0572 17.507 12.442 17.507 12.91C17.507 13.3781 17.8918 13.7629 18.3598 13.7629C18.8279 13.7629 19.2127 13.3781 19.2127 12.91Z" fill="black"></path><path d="M8.07383 12.0572C7.60581 12.0572 7.22099 12.442 7.22099 12.91C7.22099 13.3781 7.60581 13.7629 8.07383 13.7629C8.54185 13.7629 8.92666 13.3781 8.92666 12.91C8.92666 12.442 8.54185 12.0572 8.07383 12.0572Z" fill="black"></path><path d="M2.78003 4.84971C2.82163 5.04732 2.90484 5.22413 3.00884 5.39054L2.45762 5.94176L2.99844 6.48258L3.54966 5.93136C3.71607 6.03536 3.89288 6.10816 4.09048 6.16017V6.9402H4.86011V6.16017C5.05772 6.11857 5.23453 6.03536 5.40094 5.93136L5.95216 6.48258L6.49298 5.94176L5.94176 5.39054C6.04576 5.22413 6.11857 5.04732 6.17057 4.84971H6.9506V4.08008H6.17057C6.12897 3.88248 6.04576 3.70567 5.94176 3.53926L6.49298 2.98804L5.95216 2.44722L5.40094 2.99844C5.23453 2.89444 5.05772 2.82163 4.86011 2.76963V2H4.09048V2.78003C3.89288 2.82163 3.71607 2.90484 3.54966 3.00884L2.99844 2.45762L2.45762 2.99844L3.00884 3.54966C2.90484 3.71607 2.83203 3.89288 2.78003 4.09048H2V4.86011H2.78003V4.84971ZM3.49766 4.4649C3.49766 3.93448 3.93448 3.49766 4.4649 3.49766C4.99532 3.49766 5.43214 3.93448 5.43214 4.4649C5.43214 4.99532 4.99532 5.43214 4.4649 5.43214C3.93448 5.43214 3.49766 4.99532 3.49766 4.4649Z" fill="black"></path></svg></svg>
			<span class="health-activities__item__name">Spore</span>
			<span class="health-activities__item__category" style="border-right: 3px solid #f05514">Alto</span>
			<span class="health-activities__item__category__unsupported" style="border-right: 3px solid transparent">Dati non supportati in questa posizione</span>
		</a>
		<a data-slug="grass-pollen" href="/it/it/rome/213490/allergies-weather/213490?name=grass-pollen" class="health-activities__item show " style="border-right-color: #93c701;">
			<svg class="health-activities__item__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M19.9016 21.0594H18.8976V20.8687C19.1486 14.2622 21.257 12.8667 21.498 12.7261L22 13.5996C22 13.5996 20.1325 14.8546 19.9116 20.8887V21.0594H19.9016Z" fill="black"></path><path d="M17.4618 21.0594H16.4578V20.8887C16.3775 17.0735 14.6205 14.8245 14.5803 14.7843L15.3635 14.1518C15.4137 14.2221 16.2972 15.3165 16.8996 17.2643C17.3715 14.9751 18.3655 12.0333 20.4438 9.81446L21.1767 10.4972C17.6325 14.2924 17.4719 20.5875 17.4618 20.8486V21.0594Z" fill="black"></path><path d="M11.9197 21.1297C11.8695 20.8185 11.8494 20.5173 11.8494 20.2261C11.8494 17.8365 13.2249 15.8486 13.2851 15.7482L14.1084 16.3205C14.1084 16.3205 12.8534 18.1578 12.8534 20.2261C12.8534 20.4671 12.8735 20.7181 12.9137 20.9691L11.9197 21.1197V21.1297Z" fill="black"></path><path d="M10.3133 21.0594H9.30923V20.8687C9.30923 20.5373 9.56024 13.1076 12.753 8.951L13.5462 9.56345C10.5542 13.449 10.3133 20.8084 10.3133 20.8787V21.0494V21.0594Z" fill="black"></path><path d="M7.85341 21.0594H6.84939V20.8787C6.76907 15.6277 4.23895 11.5213 4.20883 11.4811L5.06224 10.949C5.14257 11.0695 6.43775 13.1879 7.24096 16.3506C7.69276 13.2783 8.6767 9.23212 10.7851 6.2L11.6084 6.77229C7.95381 12.0132 7.85341 20.7984 7.85341 20.8787V21.0594Z" fill="black"></path><path d="M4.69076 21.1297L3.69679 20.9891C3.69679 20.9891 3.74699 20.5976 3.74699 19.965C3.74699 18.6096 3.50602 16.1297 2 13.7904L2.84337 13.2482C4.47992 15.7883 4.751 18.4389 4.751 19.9249C4.751 20.6277 4.69076 21.0695 4.68072 21.1297H4.69076Z" fill="black"></path></svg></svg>
			<span class="health-activities__item__name">Polline dell’erba</span>
			<span class="health-activities__item__category" style="border-right: 3px solid #93c701">Bassa</span>
			<span class="health-activities__item__category__unsupported" style="border-right: 3px solid transparent">Dati non supportati in questa posizione</span>
		</a>
		<a data-slug="dust-dander" href="/it/it/rome/213490/allergies-weather/213490?name=dust-dander" class="health-activities__item show " style="border-right-color: #f05514;">
			<svg class="health-activities__item__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.3491 22.0558C10.1262 22.0558 9.01184 21.3852 8.44971 20.3596C8.20316 20.3892 7.95661 20.4089 7.71007 20.4089C4.76135 20.4089 2.3649 18.1012 2.3649 15.2609C2.3649 12.4207 4.76135 10.1032 7.71007 10.1032C7.91717 10.1032 8.12427 10.113 8.33137 10.1426C8.41026 10.1426 8.48916 10.1623 8.56805 10.1722C9.09074 10.2511 9.60356 10.4089 10.0769 10.6456L9.65287 11.5331C9.25839 11.3458 8.84419 11.2176 8.42013 11.1485L8.22289 11.1189C8.05523 11.0992 7.88758 11.0894 7.71007 11.0894C5.31362 11.0894 3.36095 12.9533 3.36095 15.2511C3.36095 17.5489 5.31362 19.4227 7.71007 19.4227C8.01579 19.4227 8.33137 19.3931 8.63709 19.3241L9.04143 19.2353L9.18936 19.6199C9.52466 20.4779 10.3925 21.0598 11.3491 21.0598C12.1972 21.0598 12.9763 20.616 13.3807 19.9059L13.5582 19.5903L13.9132 19.6692C14.3274 19.7678 14.7712 19.8172 15.215 19.8172C18.4103 19.8172 21.0138 17.3221 21.0138 14.255C21.0138 11.188 18.4103 8.6929 15.215 8.6929C14.4951 8.6929 13.7949 8.82111 13.1341 9.05779L12.789 8.13077C13.5582 7.84478 14.3767 7.69685 15.215 7.69685C18.9527 7.69685 22 10.6357 22 14.2452C22 17.8546 18.9527 20.7935 15.215 20.7935C14.8107 20.7935 14.4162 20.7639 14.0316 20.6949C13.4201 21.5331 12.4142 22.046 11.3393 22.046L11.3491 22.0558Z" fill="black"></path><path d="M7.19724 4.55089C7.19724 4.19586 6.91124 3.9 6.54635 3.9C6.18146 3.9 5.89546 4.186 5.89546 4.55089C5.89546 4.91578 6.18146 5.20178 6.54635 5.20178C6.91124 5.20178 7.19724 4.91578 7.19724 4.55089Z" fill="black"></path><path d="M5.24457 6.49369C5.24457 6.13866 4.95857 5.8428 4.59368 5.8428C4.22879 5.8428 3.94279 6.1288 3.94279 6.49369C3.94279 6.85858 4.22879 7.14458 4.59368 7.14458C4.95857 7.14458 5.24457 6.85858 5.24457 6.49369Z" fill="black"></path><path d="M8.49902 7.14458C8.85405 7.14458 9.1499 6.85858 9.1499 6.49369C9.1499 6.1288 8.86391 5.8428 8.49902 5.8428C8.13413 5.8428 7.84813 6.1288 7.84813 6.49369C7.84813 6.85858 8.13413 7.14458 8.49902 7.14458Z" fill="black"></path><path d="M3.30177 8.44635C3.30177 8.09132 3.01578 7.79546 2.65089 7.79546C2.286 7.79546 2 8.08146 2 8.44635C2 8.81124 2.286 9.09724 2.65089 9.09724C3.01578 9.09724 3.30177 8.81124 3.30177 8.44635Z" fill="black"></path><path d="M11.0927 8.44635C11.0927 8.09132 10.8067 7.79546 10.4418 7.79546C10.0769 7.79546 9.79092 8.08146 9.79092 8.44635C9.79092 8.81124 10.0769 9.09724 10.4418 9.09724C10.8067 9.09724 11.0927 8.81124 11.0927 8.44635Z" fill="black"></path><path d="M7.19724 8.44635C7.19724 8.09132 6.91124 7.79546 6.54635 7.79546C6.18146 7.79546 5.89546 8.08146 5.89546 8.44635C5.89546 8.81124 6.18146 9.09724 6.54635 9.09724C6.91124 9.09724 7.19724 8.81124 7.19724 8.44635Z" fill="black"></path><path d="M14.5049 17.0065C14.5049 17.3615 14.7909 17.6574 15.1558 17.6574C15.5207 17.6574 15.8067 17.3714 15.8067 17.0065C15.8067 16.6416 15.5207 16.3556 15.1558 16.3556C14.7909 16.3556 14.5049 16.6416 14.5049 17.0065Z" fill="black"></path><path d="M16.4477 15.0637C16.4477 15.4187 16.7337 15.7146 17.0986 15.7146C17.4635 15.7146 17.7495 15.4286 17.7495 15.0637C17.7495 14.6988 17.4635 14.4128 17.0986 14.4128C16.7337 14.4128 16.4477 14.6988 16.4477 15.0637Z" fill="black"></path><path d="M12.5523 15.0637C12.5523 15.4187 12.8383 15.7146 13.2031 15.7146C13.568 15.7146 13.854 15.4286 13.854 15.0637C13.854 14.6988 13.568 14.4128 13.2031 14.4128C12.8383 14.4128 12.5523 14.6988 12.5523 15.0637Z" fill="black"></path><path d="M18.4004 13.111C18.4004 13.4661 18.6864 13.7619 19.0513 13.7619C19.4162 13.7619 19.7022 13.4759 19.7022 13.111C19.7022 12.7462 19.4162 12.4602 19.0513 12.4602C18.6864 12.4602 18.4004 12.7462 18.4004 13.111Z" fill="black"></path><path d="M10.5996 13.111C10.5996 13.4661 10.8856 13.7619 11.2505 13.7619C11.6154 13.7619 11.9014 13.4759 11.9014 13.111C11.9014 12.7462 11.6154 12.4602 11.2505 12.4602C10.8856 12.4602 10.5996 12.7462 10.5996 13.111Z" fill="black"></path><path d="M14.5049 13.111C14.5049 13.4661 14.7909 13.7619 15.1558 13.7619C15.5207 13.7619 15.8067 13.4759 15.8067 13.111C15.8067 12.7462 15.5207 12.4602 15.1558 12.4602C14.7909 12.4602 14.5049 12.7462 14.5049 13.111Z" fill="black"></path></svg></svg>
			<span class="health-activities__item__name">Polvere e forfora animale</span>
			<span class="health-activities__item__category" style="border-right: 3px solid #f05514">Alto</span>
			<span class="health-activities__item__category__unsupported" style="border-right: 3px solid transparent">Dati non supportati in questa posizione</span>
		</a>
	<div class="health-activities__copernicus">
		Include informazioni Copernicus Atmosphere Monitoring Service modificate 2026
	</div>
</div>


	

	

			</div>
			
			
				<div class="more-cta-links"></div>
			
		</div>
		
			<div class="page-column-2">
				
	
<div class="right-rail">
	<div class="glacier-ad unrendered top_right config-top_right content-module" ad-type="top_right" id="top_right" data-google-query-id="CNH1x66V_JMDFXcEVQgdJnsZ9w"><div id="google_ads_iframe_/6581/web/it/top_right/weather/local_home_0__container__" style="border: 0pt; margin: auto; text-align: center; width: 300px; height: 250px;"><iframe frameborder="0" src="https://2810cda93e3ea9046645a1a797ccdabf.safeframe.googlesyndication.com/safeframe/1-0-45/html/container.html" id="google_ads_iframe_/6581/web/it/top_right/weather/local_home_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="300" height="250" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" aria-label="Advertisement" tabindex="0" data-google-container-id="2" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div>

	
	
	<div class="glacier-ad unrendered bottom_right config-bottom_right content-module" ad-type="bottom_right" id="bottom_right" data-google-query-id="CMuNyK6V_JMDFXCMgwcd2p0Upw"><script src="https://securepubads.g.doubleclick.net/gampad/adx?iu=/6581/web/postbid/bottom_right/weather/local_home&amp;sz=300x250&amp;c=1776679087&amp;t=fdate%3D20260420%26lang%3Dit%26ut%3D1%26advelvet%3D5%26inview%3Dititrome213490weather-forecast213490%3Awbr%2Cwb%26bot%3D0%26pgview%3D1%26partner%3Dgoogle_search_accuweather%26ufdb%3DLII7%26city%3DRome%26country%3DIT%26state%3D62%26dma%3Dnull%26key%3D213490%26region%3Deur%26lat%3D41.901%26lon%3D12.48%26browser%3Dsafari%26connection%3Dmobile_vhigh_5000%26wx_seg%3D101100100%2C102102102%2C109101100%2C108102100%2C100108101%2C102100100%2C102101100%2C102103100%2C107100102%2C100111100%2C107101102%2C108103101%2C101103100%2C100113103%2C108104101%2C101105100%2C110100100%2C109104100%2C109105100%2C100106102%2C110101101%2C109100102%2C108101102%2C103100102%2C109103102%2C103101102%2C101106102%2C108100102%2C100109105%2C102104102%2C104100103%2C101104101%2C104101101%2C100109102%2C109102102%2C100114105%2C109106102%2C101107101%2C101108101%2C101102102%2C105100102%2C107103102%2C100114102%2C100114101%2C101101101%26alertscategory%3DSEVERE%2CSEVERE%26alertssource%3Dit%2Cit%26alertstypeid%3DIT312%2CIT312%26cuhd%3D64%26cuhi%3D67%26cuuv%3D6%26cuwd%3D8%26cuwx%3D3%26realfeel%3D75%2Ca80%2Cb75%2Cc75%2Cd75%26cuaq%3D3%26fc1hi%3D74%26fc1lo%3D54%26fc1wx%3D2%26lfscategory%3Drain%26lfsday%3D3%26lfsseverity%3D5%26lfs%3D5_rain_3%26pt%3D15918%26userid%3Dactive%26userid3p%3Dmissing%26sub%3Dfree%26auth%3Dfalse%26site%3Ddesktop%26hour%3D11%26viewport%3D1470x840%26iabctax%3DIAB15-10%2CIAB20-14%2CIAB20-19%2C390%2C659%26from%3Dnull%26interstitial%3D0%26upr%3D0.1%26upr_0%3Dno_bid%26upr_auction%3Dprebid%26userid3pbid%3Dmissing-no_bid%26hb_bid_1st%3Dno_bid%26hb_bid_2nd%3Dno_bid%26ppid%3D7d695715xd89fx4158xab9bx5114c8ba51db&amp;m=text/javascript"></script><ins class="adsbygoogle" style="display:inline-block;margin:0 auto;width:300px;height:250px;" data-ad-client="ca-pub-5771594739411148" data-ad-slot="9359203321" data-adsbygoogle-status="done" data-ad-status="filled"><div id="aswift_1_host" style="border: medium; height: 250px; width: 300px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0;width:300px;height:250px;min-height:auto;max-height:none;min-width:auto;max-width:none;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" src="https://googleads.g.doubleclick.net/pagead/ads?gdpr=1&amp;us_privacy=1---&amp;gdpr_consent=CQi9j0AQi9j0AFUABAENCaFsAP_gAEPgACiQJzQKwAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoASQAmABRAC3AF4AXwAwgCAAEFAI4AjwBKACcAFIALkAZQA5wB3AEIAMaAacA6oB7QEagKbAVcAvMBjIDJAGTgPMAf4BGYCcwJzQJgAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoATAAogBbgC8AL4AYQBAACCgEcAR4AnABSADKAHOAO4AhABjQDTgHtAU2Aq4BeYDGQGSAMnAeYA_wCMwE5gAA.IJzQKwAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoASQAmABRAC3AF4AXwAwgCAAEFAI4AjwBKACcAFIALkAZQA5wB3AEIAMaAacA6oB7QEagKbAVcAvMBjIDJAGTgPMAf4BGYCcwAAA.f_wACHwAAAAA&amp;addtl_consent=2~70.1092.3130&amp;gpp_sid=-1&amp;client=ca-pub-5771594739411148&amp;output=html&amp;h=250&amp;slotname=9359203321&amp;adk=1225942916&amp;adf=3672151656&amp;pi=t.ma~as.9359203321&amp;w=300&amp;lmt=1776679088&amp;format=300x250&amp;url=https%3A%2F%2Fwww.accuweather.com%2Fit%2Fit%2Frome%2F213490%2Fweather-forecast%2F213490&amp;aiof=9&amp;asro=0&amp;aiapmid=0.0001&amp;aiactd=0&amp;aicctd=0&amp;ailctd=0&amp;aimartd=4&amp;aieuf=1&amp;aicrs=1&amp;abgtt=6&amp;dt=1776679087579&amp;bpp=1&amp;bdt=11661&amp;idt=545&amp;shv=r20260415&amp;mjsv=m202604140101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D50b54bc676f3e279%3AT%3D1776353262%3ART%3D1776679086%3AS%3DALNI_MaYJn7Rj3fos7s6RW40iAkrmQwNRQ&amp;gpic=UID%3D000013a4a1bbcb98%3AT%3D1776353262%3ART%3D1776679086%3AS%3DALNI_MauOrbmlYjxtpVhWC264qsoeA92Ow&amp;eo_id_str=ID%3D724a6266e0a68339%3AT%3D1776353262%3ART%3D1776679086%3AS%3DAA-Afjbd8FlTRWtWRf5qdeFKs2Ny&amp;prev_fmts=0x0&amp;nras=1&amp;correlator=2027352221728&amp;frm=20&amp;pv=1&amp;u_tz=120&amp;u_his=3&amp;u_h=833&amp;u_w=1470&amp;u_ah=833&amp;u_aw=1470&amp;u_cd=24&amp;u_sd=2&amp;adx=913&amp;ady=679&amp;biw=1470&amp;bih=833&amp;scr_x=0&amp;scr_y=494&amp;eid=95385799%2C95387509%2C95388457%2C95387625%2C95386955&amp;oid=2&amp;pvsid=6504820882849348&amp;tmod=1857319862&amp;uas=3&amp;nvt=1&amp;fc=1920&amp;brdim=0%2C0%2C0%2C0%2C1470%2C0%2C1470%2C833%2C1470%2C833&amp;vis=1&amp;rsz=%7C%7CoeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=0&amp;bc=31&amp;plas=241x658_l%7C241x658_r&amp;bz=1&amp;ifi=8&amp;uci=a!8&amp;fsb=1&amp;dtd=548" data-google-container-id="a!8" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CM30y6-V_JMDFXUTigMdRAolIQ" data-load-complete="true"></iframe></div></ins></div>

	
</div>


			</div>
		
	</div>
	
		<div class="glacier-ad unrendered bottom config-bottom content-module" ad-type="bottom" id="bottom" data-google-query-id="CI_fz7CV_JMDFYrORAcd5oo39w"><div id="google_ads_iframe_/6581/web/it/bottom/weather/local_home_0__container__" style="border: 0pt; margin: auto; text-align: center; width: 970px; height: 250px;"><iframe frameborder="0" src="https://2810cda93e3ea9046645a1a797ccdabf.safeframe.googlesyndication.com/safeframe/1-0-45/html/container.html" id="google_ads_iframe_/6581/web/it/bottom/weather/local_home_0" title="Contenuto dell'annuncio di terze parti" name="" scrolling="no" marginwidth="0" marginheight="0" width="970" height="250" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" aria-label="Pubblicità" tabindex="0" data-google-container-id="7" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div><div id="bottom-dawn" style="position: absolute; inset: 0px; visibility: hidden; opacity: 0; pointer-events: none; z-index: 1;"><div id="google_ads_iframe_/6581/web/it/bottom/weather/breaking_dawn_0__container__" style="border: 0pt; margin: auto; text-align: center;"></div></div>

	
	
		<div class="breadcrumbs ">
	<div class="crumbs">
			<a href="/it/world-weather" class="breadcrumbs__link">Mondo</a>
			<svg class="breadcrumbs__chevron chevron-icon right" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
			<a href="/it/europe-weather" class="breadcrumbs__link">Europa</a>
			<svg class="breadcrumbs__chevron chevron-icon right" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
			<a href="/it/it/italy-weather" class="breadcrumbs__link">Italia</a>
			<svg class="breadcrumbs__chevron chevron-icon right" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
			<a href="/it/it/62/lazio-weather" class="breadcrumbs__link">Lazio</a>
			<svg class="breadcrumbs__chevron chevron-icon right" xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6"><path d="M10 .969L9.037 0 5 4.063.963 0 0 .969 5 6z"></path></svg>
			<a href="/it/it/rome/213490/weather-forecast/213490" class="breadcrumbs__link">Roma</a>
			
	</div>
</div>

	
	
		
<div class="neighbors-wrapper">
	<div class="neighbors-wrapper__content">
			<h2 class="neighbors-title">Luoghi vicini:</h2>
		<div class="neighbors-scroll">
			<ul id="neighbors" class="neighbor-items">
					<li class="neighbor-item" itemprop="address" itemscope="true" itemtype="https://schema.org/PostalAddress">
						<a href="/it/it/acilia-castel-fusano-ostia-antica/2567497/weather-forecast/2567497" class="neighbor-link" data-from-string="nearby_locations">
							<span itemprop="addressLocality">Acilia-Castel Fusano-Ostia Antica</span>,
							<span itemprop="addressRegion">Lazio</span>
						</a>
					</li>
					<li class="neighbor-item" itemprop="address" itemscope="true" itemtype="https://schema.org/PostalAddress">
						<a href="/it/it/frascati/213390/weather-forecast/213390" class="neighbor-link" data-from-string="nearby_locations">
							<span itemprop="addressLocality">Frascati</span>,
							<span itemprop="addressRegion">Lazio</span>
						</a>
					</li>
					<li class="neighbor-item" itemprop="address" itemscope="true" itemtype="https://schema.org/PostalAddress">
						<a href="/it/it/ostia/2567489/weather-forecast/2567489" class="neighbor-link" data-from-string="nearby_locations">
							<span itemprop="addressLocality">Lido di Ostia</span>,
							<span itemprop="addressRegion">Lazio</span>
						</a>
					</li>
			</ul>
		</div>
	</div>
</div>

	
	<div class="base-footer   ">
	<span class="">
	</span>
	<div class="footer-legalese">
	<div class="footer-copyright">
		<span>
			© 2026 AccuWeather, Inc. "AccuWeather" e il logo del sole sono marchi registrati di AccuWeather, Inc. Tutti i diritti riservati.

		</span>
	</div>
	<div id="footer-terms" class="footer-terms">
		<a data-ga="Terms of Use" href="/it/legal" target="_blank">
			Condizioni di utilizzo
		</a>
		|
		<a data-ga="Privacy Policy" href="/it/privacy" target="_blank">
			Informativa sulla privacy
		</a>
		|
		<a data-ga="Cookie Policy" href="/it/cookiepolicy" target="_blank">
			Norme sui cookie
		</a>
		|
		<a data-ga="Data Sources" href="/it/data-sources" target="_blank">
			Fonti dei dati
		</a>
	</div>
</div>

</div>

	
</div><iframe name="__gppLocator" style="display: none;"></iframe><iframe name="__tcfapiLocator" style="display: none;"></iframe>


	<script>
		// Check for third party cookie support
		const thirdPartyIframe = document.createElement('iframe');
		thirdPartyIframe.setAttribute(
			'src',
			'https://www.awxcdn.com/adc/3rdpartycheck.html'
		);
		thirdPartyIframe.setAttribute('style', 'width:0;height:0;display:none');
		document.body.appendChild(thirdPartyIframe);
	</script><iframe src="https://www.awxcdn.com/adc/3rdpartycheck.html" style="width:0;height:0;display:none"></iframe>

		

			<script charset="utf-8" src="https://www.awxcdn.com/adc-assets/bundles/city.three-day-desktop.e8554de08f35914a35cb.js" async=""></script>

			<script charset="utf-8" src="https://www.awxcdn.com/adc-assets/bundles/legacy-header.59998cf2e2a578ed27b9.js" async=""></script>



	

    <script>
        window.tagEngineDataLayer = window.tagEngineDataLayer || {};
        window.tagEngineDataLayer.comScore = {
            cs_fpid: "aabb62c2-3a89-44c2-86c5-ead1b04c96df",
            c4: "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490",
            c7: "https://www.accuweather.com/it/it/rome/213490/weather-forecast/213490",
            c8: "Roma, Lazio, Italia Previsioni meteo tre giorni | AccuWeather",
            c9: "https://www.google.com/"
        };
    </script>

	


<script>
	var isPushlyEnabled = false;
</script>


		<script>
		function callBlockthroughScript() {
			if (window.supportsAds == true) {
				return;
			}

			const scriptEl = document.getElementById('bt_bootstrap_2.0');
			if (!scriptEl) {
				const s = document.createElement("script");
				const el = document.getElementsByTagName("script")[0];
				s.setAttribute('id', 'bt_bootstrap_2.0');
				s.async = true;
				s.src = "https://btloader.com/tag?o=5673795450830848&upapi=true";
				el.parentNode.insertBefore(s, el);
			}
		};

			if (typeof window.ketch === 'function') {
				window.ketch('on', 'consent', () => {
					window.addEventListener('DOMContentLoaded', callBlockthroughScript);
					setTimeout(callBlockthroughScript, 15000);
				});
			} else {
				window.addEventListener('DOMContentLoaded', callBlockthroughScript);
				setTimeout(callBlockthroughScript, 15000);
			}
				</script>

	

	<script>
		try {
		;
		} catch (error) { }
	</script>
	<script async="" src="https://www.accuweather.com/tags/common/body/ad-script-3333932b.js"></script>
	<script async="" src="https://www.accuweather.com/tags/glacier/body/search-bar-ad-5d1d21c7.js"></script><script>(async () => {(function(){function m(n,e){const c="https://sb.scorecardresearch.com/p?",t=Array.from(document.querySelectorAll('img[src^="'+c+'"]'));if(t.find(s=>s.src.includes(`cs_ucfr=${n}`)))return;const o=t.find(s=>s.src.includes("cs_ucfr=")&&!s.src.includes(`cs_ucfr=${n}`));o&&o.remove();const d=`${c}cs_fpid=${e.cs_fpid}&cs_fpit=c&c1=2&c2=6005068&c4=${encodeURIComponent(e.c4)}&c7=${encodeURIComponent(e.c7)}&c8=${encodeURIComponent(e.c8)}&c9=${encodeURIComponent(e.c9)}&cs_ucfr=${n}`,i=document.createElement("img");i.src=d,i.alt="ComScore",i.style.display="none",document.body.appendChild(i)}function a(){const n=window.tagEngineDataLayer?.comScore;if(!n)return;const e=100,c=2e3;let t=0;const r=()=>{typeof window.ketch=="function"?window.ketch("on","consent",function(o){const d=o?.purposes?.targeted_advertising;m(d===!0?1:0,n)}):t<c&&(t+=e,setTimeout(r,e))};r()}document.readyState==="complete"||document.readyState==="interactive"?a():document.addEventListener("DOMContentLoaded",a)})();
//# sourceMappingURL=comscore.inline.5-abc6ca40.js.map
})();</script>
<noscript><img src="https://www.accuweather.com/akam/13/pixel_15c10ccf?a=dD0yYWUzYWNmMDdlYzhiODFiZWMxYjAxMTA1ZGMzMzUyMDFjMWJkNDU5JmpzPW9mZg==" style="visibility: hidden; position: absolute; left: -999px; top: -999px;" /></noscript>


<iframe src="https://www.awxcdn.com/adc/3rdpartycheck.html" style="width:0;height:0;display:none"></iframe><iframe marginwidth="0" marginheight="0" scrolling="no" frameborder="0" id="13a3658de884f38" width="0" height="0" src="about:blank" name="__pb_locator__" style="display: none; height: 0px; width: 0px; border: 0px;"></iframe><img src="https://sb.scorecardresearch.com/p?cs_fpid=aabb62c2-3a89-44c2-86c5-ead1b04c96df&amp;cs_fpit=c&amp;c1=2&amp;c2=6005068&amp;c4=https%3A%2F%2Fwww.accuweather.com%2Fit%2Fit%2Frome%2F213490%2Fweather-forecast%2F213490&amp;c7=https%3A%2F%2Fwww.accuweather.com%2Fit%2Fit%2Frome%2F213490%2Fweather-forecast%2F213490&amp;c8=Roma%2C%20Lazio%2C%20Italia%20Previsioni%20meteo%20tre%20giorni%20%7C%20AccuWeather&amp;c9=https%3A%2F%2Fwww.google.com%2F&amp;cs_ucfr=1" alt="ComScore" style="display: none;"><iframe name="__uspapiLocator" style="display: none;"></iframe><iframe name="google_ads_top_frame" id="google_ads_top_frame" style="display: none; position: fixed; left: -999px; top: -999px; width: 0px; height: 0px;"></iframe><iframe src="https://www.google.com/recaptcha/api2/aframe" width="0" height="0" style="display: none;"></iframe><div><iframe src="https://google-bidout-d.openx.net/w/1.0/pd?plm=5" width="0" height="0" style="display:none;"></iframe></div><ins class="adsbygoogle adsbygoogle-noablate" data-ad-hi="true" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_0_host" style="border: medium; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;min-height:auto;max-height:none;min-width:auto;max-width:none;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" src="https://googleads.g.doubleclick.net/pagead/ads?gdpr=1&amp;us_privacy=1---&amp;gdpr_consent=CQi9j0AQi9j0AFUABAENCaFsAP_gAEPgACiQJzQKwAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoASQAmABRAC3AF4AXwAwgCAAEFAI4AjwBKACcAFIALkAZQA5wB3AEIAMaAacA6oB7QEagKbAVcAvMBjIDJAGTgPMAf4BGYCcwJzQJgAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoATAAogBbgC8AL4AYQBAACCgEcAR4AnABSADKAHOAO4AhABjQDTgHtAU2Aq4BeYDGQGSAMnAeYA_wCMwE5gAA.IJzQKwAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoASQAmABRAC3AF4AXwAwgCAAEFAI4AjwBKACcAFIALkAZQA5wB3AEIAMaAacA6oB7QEagKbAVcAvMBjIDJAGTgPMAf4BGYCcwAAA.f_wACHwAAAAA&amp;addtl_consent=2~70.1092.3130&amp;gpp_sid=-1&amp;client=ca-pub-5771594739411148&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1776679088&amp;plaf=1%3A2%2C2%3A2%2C7%3A2&amp;plat=1%3A192%2C2%3A192%2C3%3A128%2C4%3A128%2C8%3A192%2C9%3A32776%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32%2C41%3A32%2C42%3A32%2C43%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.accuweather.com%2Fit%2Fit%2Frome%2F213490%2Fweather-forecast%2F213490&amp;pra=5&amp;aiof=9&amp;asro=0&amp;aiapmid=0.0001&amp;aiactd=0&amp;aicctd=0&amp;ailctd=0&amp;aimartd=4&amp;aieuf=1&amp;aicrs=1&amp;abgtt=6&amp;dt=1776679087578&amp;bpp=1&amp;bdt=11660&amp;idt=530&amp;shv=r20260415&amp;mjsv=m202604140101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D50b54bc676f3e279%3AT%3D1776353262%3ART%3D1776679086%3AS%3DALNI_MaYJn7Rj3fos7s6RW40iAkrmQwNRQ&amp;gpic=UID%3D000013a4a1bbcb98%3AT%3D1776353262%3ART%3D1776679086%3AS%3DALNI_MauOrbmlYjxtpVhWC264qsoeA92Ow&amp;eo_id_str=ID%3D724a6266e0a68339%3AT%3D1776353262%3ART%3D1776679086%3AS%3DAA-Afjbd8FlTRWtWRf5qdeFKs2Ny&amp;nras=1&amp;correlator=2027352221728&amp;frm=20&amp;pv=2&amp;u_tz=120&amp;u_his=3&amp;u_h=833&amp;u_w=1470&amp;u_ah=833&amp;u_aw=1470&amp;u_cd=24&amp;u_sd=2&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1470&amp;bih=833&amp;scr_x=0&amp;scr_y=475&amp;eid=95385799%2C95387509%2C95388457%2C95387625%2C95386955&amp;oid=2&amp;pvsid=6504820882849348&amp;tmod=1857319862&amp;uas=3&amp;nvt=1&amp;fsapi=1&amp;fc=1920&amp;brdim=0%2C0%2C0%2C0%2C1470%2C0%2C1470%2C833%2C1470%2C833&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;plas=241x658_l%7C241x658_r&amp;bz=1&amp;ifi=7&amp;uci=a!7&amp;fsb=1&amp;dtd=543" data-google-container-id="a!7" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true"></iframe></div></ins><iframe src="https://gum.criteo.com/syncframe?origin=publishertagids&amp;topUrl=www.accuweather.com&amp;gdpr=1&amp;gdpr_consent=CQi9j0AQi9j0AFUABAENCaFsAP_gAEPgACiQJzQKwAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoASQAmABRAC3AF4AXwAwgCAAEFAI4AjwBKACcAFIALkAZQA5wB3AEIAMaAacA6oB7QEagKbAVcAvMBjIDJAGTgPMAf4BGYCcwJzQJgAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoATAAogBbgC8AL4AYQBAACCgEcAR4AnABSADKAHOAO4AhABjQDTgHtAU2Aq4BeYDGQGSAMnAeYA_wCMwE5gAA.IJzQKwAAwAKAAyAB4AIAAVgAuADIAHAAQAAkABkADQAIoASQAmABRAC3AF4AXwAwgCAAEFAI4AjwBKACcAFIALkAZQA5wB3AEIAMaAacA6oB7QEagKbAVcAvMBjIDJAGTgPMAf4BGYCcwAAA.f_wACHwAAAAA&amp;gpp=DBAA&amp;gpp_sid=-1#{&quot;bundle&quot;:{&quot;value&quot;:&quot;9bKLTV9LOTVRWjBITXJMN3d6T0V3ODcwRmpMWnJLNFN6VTJIc1h4TiUyRiUyRlolMkY3Ynk4S2hkMHF3aEMzM3BDUVF5QWtzZUpEY1JoQkx5NEdQSVVvdGt1dVZrdFVhUlZzeEFpZGtUWmVhMHJoanJWRm5GMlYlMkZNS0h6cyUyRkwlMkIlMkZ5MXRnWGVodTRORVlZZ1JHY1J2ZGFidm12QTZ0MDdTSiUyRnFXVlRWTmVXZGtJcllMSFJ2OVZvJTNE&quot;,&quot;origin&quot;:3},&quot;optout&quot;:{&quot;value&quot;:false,&quot;origin&quot;:0},&quot;tld&quot;:&quot;accuweather.com&quot;,&quot;topUrl&quot;:&quot;www.accuweather.com&quot;,&quot;version&quot;:106267,&quot;origin&quot;:&quot;publishertagids&quot;,&quot;requestId&quot;:&quot;0.9035721336528879&quot;}" width="0" height="0" frameborder="0" sandbox="allow-scripts allow-same-origin" aria-hidden="true" tabindex="-1" title="Criteo GUM iframe" style="border-width: 0px; margin: 0px; display: none;"></iframe></body><ins id="gpt_unit_/6581/web/it/interstitial/weather/local_home_0" data-google-query-id="CIqH3K6V_JMDFUP7EQgdomwRjw" aria-hidden="true" style="display: none !important; width: 100vw !important; height: 100vh !important; inset: 0px auto auto 0px !important; clear: none !important; float: none !important; margin: 0px !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; padding: 0px !important; position: fixed !important; vertical-align: baseline !important; visibility: visible !important; z-index: 2147483647 !important; background: 0% 0% repeat !important;" data-vignette-loaded="true" tabindex="0"><div id="google_ads_iframe_/6581/web/it/interstitial/weather/local_home_0__container__" style="border: 0pt !important; margin: auto !important; text-align: center !important; width: 100vw !important; height: 100vh !important; inset: auto !important; clear: none !important; display: inline !important; float: none !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; padding: 0px !important; position: static !important; vertical-align: baseline !important; visibility: visible !important; z-index: auto !important;"><iframe frameborder="0" src="https://2810cda93e3ea9046645a1a797ccdabf.safeframe.googlesyndication.com/safeframe/1-0-45/html/container.html" id="google_ads_iframe_/6581/web/it/interstitial/weather/local_home_0" title="Contenuto dell'annuncio di terze parti" name="" scrolling="no" marginwidth="0" marginheight="0" width="" height="" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" allow="autoplay" aria-label="Pubblicità" tabindex="0" data-google-container-id="5" style="border: 0px !important; vertical-align: bottom !important; width: 100vw !important; height: 100vh !important; inset: 0px auto auto 0px !important; position: absolute !important; clear: none !important; display: inline !important; float: none !important; margin: 0px !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; padding: 0px !important; visibility: visible !important; z-index: auto !important;" data-load-complete="true"></iframe></div></ins><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20260415/r20190131/zrt_lookup_fy2021.html" style="display: none;"></iframe></html>"""

gold_text = """OGGI
ORARIO
10 GIORNI
RADAR
MINUTECAST®
MENSILE
QUALITÀ DELL'ARIA
SALUTE E ATTIVITÀ

2
Allarme giallo per temporali
METEO ATTUALE
11:57

21°C
RealFeel® 24°
Parzialmente soleggiato
ALTRI DETTAGLI
RealFeel Shade™
19°
Vento
ESE 12 km/h
Raffiche vento
25 km/h
Qualità dell'aria
Sfavorev.
EVOLUZIONE
Sono previsti rovesci mercoledì pomeriggio
ROMA - RADAR METEO
Roma - Radar meteo

Nuvole

Temperatura
PREVISIONI ORARIE

12

21°
rain drop
2%
13

22°
rain drop
1%
14

23°
rain drop
0%
15

23°
rain drop
0%
16

22°
rain drop
0%
17

22°
rain drop
0%
18

21°
rain drop
0%
19

20°
rain drop
0%
20

19°
rain drop
1%
21

17°
1%
22

16°
1%
23

16°
1%

PREVISIONI GIORNO
OGGI
20/4

23°
12°
Da soleggiato a parzialmente nuvoloso

Parzialmente nuvoloso
12%
MAR
21/4

23°
12°
Sole con qualche nuvola

Parzialmente nuvoloso
9%
MER
22/4

20°
9°
Uno o due brevi rovesci

Parzialmente nuvoloso
63%
GIO
23/4

21°
6°
Ampiamente soleggiato

Sereno
0%
VEN
24/4

23°
8°
Ampiamente soleggiato

Prevalentemente sereno
0%
SAB
25/4

23°
10°
Parzialmente soleggiato

Sereno
0%
DOM
26/4

22°
11°
Prevalentemente soleggiato

Parzialmente nuvoloso
0%
LUN
27/4

22°
11°
Prevalentemente nuvoloso

Nuvoloso
4%
MAR
28/4

22°
12°
Nuvoloso

Prevalentemente nuvoloso
25%
MER
29/4

23°
12°
Nuvole e sole

Sereno
19%
SOLE E LUNA

13 h 33 min
Alba
06:23
Tramontare
19:56

16 h 22 min
Alba
07:53
Tramontare
00:15
QUALITÀ DELL'ARIA
VISUALIZZA ALTRO
Qualità dell'aria
Sfavorev.
L'aria ha raggiunto un livello elevato di inquinamento ed è malsana per i gruppi sensibili. Riduci il tempo trascorso all'aperto se hai sintomi quali difficoltà respiratoria o irritazione della gola.
SITUAZIONE ALLERGIE
VEDI TUTTO
Polline di albero
Bassa
Polline di ambrosia
Bassa
Spore
Alto
Polline dell’erba
Bassa
Polvere e forfora animale
Alto
"""
data = [
    {
        "url": "",
        "domain": "accuweather.com",
        "title": "rome",
        "html_text": html_text,
        "gold_text": gold_text
    }
]

with open("accuweather.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("File JSON creato correttamente!")