var provinceArray = new Array("","北京","上海","天津","重庆","河北","山西","内蒙古","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","广西","海南","四川","贵州","云南","西藏","陕西","甘肃","宁夏","青海","新疆","香港","澳门","台湾");

//定义 城市 数据数组
var cityArray = new Array(); 
cityArray[0] = new Array("","");
cityArray[1] = new Array("北京","北京"); 
cityArray[2] = new Array("上海","上海"); 
cityArray[3] = new Array("天津","天津"); 
cityArray[4] = new Array("重庆","重庆"); 
cityArray[5] = new Array("河北","石家庄|邯郸|邢台|保定|张家口|承德|廊坊|唐山|秦皇岛|沧州|衡水"); 
cityArray[6] = new Array("山西","太原|大同|阳泉|长治|晋城|朔州|吕梁|忻州|晋中|临汾|运城"); 
cityArray[7] = new Array("内蒙古","呼和浩特|包头|乌海|赤峰|呼伦贝尔|阿拉善|哲里木|兴安|乌兰察布|锡林郭勒|巴彦淖尔|伊克昭"); 
cityArray[8] = new Array("辽宁","沈阳|大连|鞍山|抚顺|本溪|丹东|锦州|营口|阜新|辽阳|盘锦|铁岭|朝阳|葫芦岛"); 
cityArray[9] = new Array("吉林","长春|吉林|四平|辽源|通化|白山|松原|白城|延边"); 
cityArray[10] = new Array("黑龙江","哈尔滨|齐齐哈尔|牡丹江|佳木斯|大庆|绥化|鹤岗|鸡西|黑河|双鸭山|伊春|七台河|大兴安岭"); 
cityArray[11] = new Array("江苏","南京|镇江|苏州|南通|扬州|盐城|徐州|连云港|常州|无锡|宿迁|泰州|淮安"); 
cityArray[12] = new Array("浙江","杭州|宁波|温州|嘉兴|湖州|绍兴|金华|衢州|舟山|台州|丽水"); 
cityArray[13] = new Array("安徽","合肥|芜湖|蚌埠|马鞍山|淮北|铜陵|安庆|黄山|滁州|宿州|池州|淮南|巢湖|阜阳|六安|宣城|亳州"); 
cityArray[14] = new Array("福建","福州|厦门|莆田|三明|泉州|漳州|南平|龙岩|宁德"); 
cityArray[15] = new Array("江西","南昌|景德镇|九江|鹰潭|萍乡|新馀|赣州|吉安|宜春|抚州|上饶"); 
cityArray[16] = new Array("山东","济南|青岛|淄博|枣庄|东营|烟台|潍坊|济宁|泰安|威海|日照|莱芜|临沂|德州|聊城|滨州|菏泽"); 
cityArray[17] = new Array("河南","郑州|开封|洛阳|平顶山|安阳|鹤壁|新乡|焦作|濮阳|许昌|漯河|三门峡|南阳|商丘|信阳|周口|驻马店|济源"); 
cityArray[18] = new Array("湖北","武汉|宜昌|荆州|襄樊|黄石|荆门|黄冈|十堰|恩施|潜江|天门|仙桃|随州|咸宁|孝感|鄂州|神农架");
cityArray[19] = new Array("湖南","长沙|常德|株洲|湘潭|衡阳|岳阳|邵阳|益阳|娄底|怀化|郴州|永州|湘西|张家界"); 
cityArray[20] = new Array("广东","广州|深圳|珠海|汕头|东莞|中山|佛山|韶关|江门|湛江|茂名|肇庆|惠州|梅州|汕尾|河源|阳江|清远|潮州|揭阳|云浮"); 
cityArray[21] = new Array("广西","南宁|柳州|桂林|梧州|北海|防城港|钦州|贵港|玉林|南宁地区|柳州地区|贺州|百色|河池"); 
cityArray[22] = new Array("海南","海口|三亚|五指山"); 
cityArray[23] = new Array("四川","成都|绵阳|德阳|自贡|攀枝花|广元|内江|乐山|南充|宜宾|广安|达川|雅安|眉山|甘孜|凉山|泸州"); 
cityArray[24] = new Array("贵州","贵阳|六盘水|遵义|安顺|铜仁|黔西南|毕节|黔东南|黔南"); 
cityArray[25] = new Array("云南","昆明|大理|曲靖|玉溪|昭通|楚雄|红河|文山|思茅|西双版纳|保山|德宏|丽江|怒江|迪庆|临沧");
cityArray[26] = new Array("西藏","拉萨|日喀则|山南|林芝|昌都|阿里|那曲"); 
cityArray[27] = new Array("陕西","西安|宝鸡|咸阳|铜川|渭南|延安|榆林|汉中|安康|商洛"); 
cityArray[28] = new Array("甘肃","兰州|嘉峪关|金昌|白银|天水|酒泉|张掖|武威|定西|陇南|平凉|庆阳|临夏|甘南"); 
cityArray[29] = new Array("宁夏","银川|石嘴山|吴忠|固原|中卫"); 
cityArray[30] = new Array("青海","西宁|海东|海南|海北|黄南|玉树|果洛|海西"); 
cityArray[31] = new Array("新疆","乌鲁木齐|石河子|克拉玛依|伊犁|巴音郭楞|昌吉|克孜勒苏|博尔塔拉|吐鲁番|哈密|喀什|和田|阿克苏|阿拉尔|塔城|阿勒泰|库尔勒|五家渠|图木舒克"); 
cityArray[32] = new Array("香港","香港"); 
cityArray[33] = new Array("澳门","澳门"); 
cityArray[34] = new Array("台湾","台湾"); 

function initProvince(){
document.getElementById('selProvince').length = 0 ; 
for(i=0; i<provinceArray.length; i++){
   document.getElementById('selProvince').options[i] = new Option(provinceArray[i],provinceArray[i]);
}
getCity(document.getElementById('selProvince').options[0].value)
}

function getCity(currProvince)
{
    //当前 所选择 的 省
    var currProvince = currProvince;
    var i,j,k;
    //清空 城市 下拉选单
    document.getElementById('selCity').length = 0 ; 
    for (i = 0 ;i <cityArray.length;i++)
      {   
          //得到 当前省 在 城市数组中的位置
          if(cityArray[i][0]==currProvince)
            {   
                //得到 当前省 所辖制的 地市
                tmpcityArray = cityArray[i][1].split("|")
                  for(j=0;j<tmpcityArray.length;j++)
                  {
                    //填充 城市 下拉选单
                    document.getElementById('selCity').options[document.getElementById('selCity').length] = new Option(tmpcityArray[j],tmpcityArray[j]); 
                  }
            } 
      } 
}

function city_filter(query)
{
	$('#products-table').hide();
	$('#loading').show();
	$.ajax({
		url: "/ajax_city_filter/",
		type: "POST",
		data: query,
		dataType: "json",
		success: function(result){
			var length=result.values.length;
			if(length==0){
				$('#loading').hide();
				$('#products-table').show();
				alert('没有该城市的数据');
				return;
			}
			else{
				$('#products-table').html('');
				$('#products-table').append('<thead><tr><th>标题</th><th>价格</th><th>交易地点</th><th>发布时间</th></tr></thead><tbody>');
				for(i=0;i<length;i++){
					$('#products-table').append('<tr><td><a href="'+result.values[i].url+'" target="_blank">'+result.values[i].title+
							'</a></td><td>'+result.values[i].price+'</td><td>'+result.values[i].place+'</td><td>'+result.values[i].time+'</td></tr>'
							);	
				}
				$('#products-table').append('</tbody>');
				$('#loading').hide();
				$('#products-table').show();
			}
			} 
	});
}

$(document).ready(function(){
	initProvince();
	$("body").click(function(){
		  $(".relative-city").hide();
	  });
	$("#citykw").bind('keyup',function(){
		  $(".relative-city").hide();
		  var kw=$(this).val();
		  kw=trim(kw);
		  if(kw=='')
			   return;
		  var query={};
		  query["citykw"]=kw;
		  $.ajax({
				url: "/ajax_search_city/",
				type: "POST",
				data: query,
				dataType: "json",
				success: function(result){
					var length=result.values.length;
					if(length==0)
						return;
					if($('.relative-city-list').length)
						  $(".relative-city-ul").html("");
					for (i=0;i<length;i++){
						$(".relative-city-ul").append('<li class="relative-city-list"><a href="javascript:void(0)">'+result.values[i]+'</a></li>');
						}
					$(".relative-city").show();
					} 
			});
	});
	
	$("#citysearch").click(function(){
		  var kw=$('#citykw').val();
		  kw=trim(kw);  
		  var query={};
		  query["citykw"]=kw;
		  query["searchtype"]=1;
		  query['brandslug']=$('#brandslug').val();
		  query['modelslug']=$('#modelslug').val();
		  query['year']=$('#year').val();
		  if(kw==''){
			  city_filter(query);
			  return;
		  }
		  $.ajax({
				url: "/ajax_search_city/",
				type: "POST",
				data: query,
				dataType: "json",
				success: function(result){
					var length=result.values.length;
					if(length==0){
						alert('没有此城市。');
						return;
					}
					else{
						city_filter(query)
					}
					} 
			});
		  
	});
	$("#cityfilter").click(function(){
		  var kw=$('#selCity').val();  
		  var query={};
		  query["citykw"]=kw;
		  query['brandslug']=$('#brandslug').val();
		  query['modelslug']=$('#modelslug').val();
		  query['year']=$('#year').val();
		  city_filter(query);
	});	
	
	$(".relative-city-list").live("click",function(){
		 var value=$("a",$(this)).html();
		 $("#citykw").val(value);
		 $("#citysearch").click();
	  });
	$('#selProvince').change(function(){
		  var prov=$('#selProvince').val(); 
		  getCity(prov);
	});
})
