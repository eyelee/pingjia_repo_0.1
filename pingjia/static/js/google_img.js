$(document).ready(function(){
	var query={};
	query["kw"]=encodeURI($("#keywordtitle").html())
	$.ajax({
		url: "/ajax_image/",
		type: "POST",
		data: query,
		dataType: "json",
		success: function(result){
			$('#pic-loading').hide();
			var results=result.values;
			for(i=0;i<results.length;i++){
				if(i==0)
					$(".carousel-inner").append('<div class="item active"><img src="'+results[i]+'" width="380px" height="280px" alt="">');
				else
					$(".carousel-inner").append('<div class="item"><img src="'+results[i]+'" width="380px" height="280px" alt="">');
			}
			$(".carousel-inner").parent().append('<a class="left carousel-control" href="#myCarousel" data-slide="prev">‹</a>'+
				                             '<a class="right carousel-control" href="#myCarousel" data-slide="next">›</a>');
			$(".carousel-inner").show();	
			} 
	});
	
	$(".data-link").click(function(){
	  $(".report-link-tab").parent().removeClass('active');
      $(".data-link-tab").parent().addClass('active');
	});
})	