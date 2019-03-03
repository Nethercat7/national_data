// JavaScript Document
var CHARTS=(function(){
	var charts=function(){
		this.init=function(){
			get_data()
			toggle()
		}
	};
	//AJAX
	function get_data(){
		//请求数据
		var data_2017=$.ajax({type:'POST',url:'/data2017',dataType:'json'}),
			data_2016=$.ajax({type:'POST',url:'/data2016',dataType:'json'}),
			data_2015=$.ajax({type:'POST',url:'/data2015',dataType:'json'}),
			data_2014=$.ajax({type:'POST',url:'/data2014',dataType:'json'}),
			data_2013=$.ajax({type:'POST',url:'/data2013',dataType:'json'}),
			enrollment_rate=$.ajax({type:'POST',url:'/enrollmentRate',dataType:'json'}),
			student_rate=$.ajax({type:'POST',url:'/studentsRate',dataType:'json'}),
			gradute_rate=$.ajax({type:'POST',url:'/graduateRate',dataType:'json'}),
			gae_2017=$.ajax({type:'POST',url:'/gae2017',dataType:'json'}),
			gae_2016=$.ajax({type:'POST',url:'/gae2016',dataType:'json'}),
			gae_2015=$.ajax({type:'POST',url:'/gae2015',dataType:'json'}),
			gae_2014=$.ajax({type:'POST',url:'/gae2014',dataType:'json'}),
			gae_2013=$.ajax({type:'POST',url:'/gae2013',dataType:'json'}),
			sip_2017=$.ajax({type:'POST',url:'/sip2017',dataType:'json'}),
			sip_2016=$.ajax({type:'POST',url:'/sip2016',dataType:'json'}),
			sip_2015=$.ajax({type:'POST',url:'/sip2015',dataType:'json'}),
			sip_2014=$.ajax({type:'POST',url:'/sip2014',dataType:'json'}),
			sip_2013=$.ajax({type:'POST',url:'/sip2013',dataType:'json'});
				
			//得到数据
			$.when(data_2017,data_2016,data_2015,data_2014,data_2013,enrollment_rate,student_rate,gradute_rate,gae_2017,gae_2016,gae_2015,gae_2014,gae_2013,sip_2017,sip_2016,sip_2015,sip_2014,sip_2013).then(function(data_2017,data_2016,data_2015,data_2014,data_2013,enrollment_rate,student_rate,gradute_rate,gae_2017,gae_2016,gae_2015,gae_2014,gae_2013,sip_2017,sip_2016,sip_2015,sip_2014,sip_2013){
				var enrollment_17=[],
				enrollment_16=[],
				enrollment_15=[],
				enrollment_14=[],
				enrollment_13=[],
				students_17=[],
				students_16=[],
				students_15=[],
				students_14=[],
				students_13=[],
				graduate_17=[],
				graduate_16=[],
				graduate_15=[],
				graduate_14=[],
				graduate_13=[],
				e_rate=[],
				s_rate=[],
				g_rate=[];
					
				//遍历各年份的数据
				for(var i=0;i<data_2017[0].length;i++){
					enrollment_17.push(data_2017[0][i].enrollment)
					students_17.push(data_2017[0][i].students)
					graduate_17.push(data_2017[0][i].graduate)
				};
				for(var i=0;i<data_2016[0].length;i++){
					enrollment_16.push(data_2016[0][i].enrollment)
					students_16.push(data_2016[0][i].students)
					graduate_16.push(data_2016[0][i].graduate)
				};
				for(var i=0;i<data_2015[0].length;i++){
					enrollment_15.push(data_2015[0][i].enrollment)
					students_15.push(data_2015[0][i].students)
					graduate_15.push(data_2015[0][i].graduate)
				};
				for(var i=0;i<data_2014[0].length;i++){
					enrollment_14.push(data_2014[0][i].enrollment)
					students_14.push(data_2014[0][i].students)
					graduate_14.push(data_2014[0][i].graduate)
				};
				for(var i=0;i<data_2013[0].length;i++){
					enrollment_13.push(data_2013[0][i].enrollment)
					students_13.push(data_2013[0][i].students)
					graduate_13.push(data_2013[0][i].graduate)
				};
				
				//招生增长率
				e_rate_2017=enrollment_rate[0][0].rate2017;
				e_rate_2016=enrollment_rate[0][0].rate2016;
				e_rate_2015=enrollment_rate[0][0].rate2015;
				e_rate_2014=enrollment_rate[0][0].rate2014;
				e_rate.push(e_rate_2014,e_rate_2015,e_rate_2016,e_rate_2017);
				//在校学生增长率
				s_rate_2017=student_rate[0][0].rate2017;
				s_rate_2016=student_rate[0][0].rate2016;
				s_rate_2015=student_rate[0][0].rate2015;
				s_rate_2014=student_rate[0][0].rate2014;
				s_rate.push(s_rate_2014,s_rate_2015,s_rate_2016,s_rate_2017);
				//毕业生生增长率
				g_rate_2017=gradute_rate[0][0].rate2017;
				g_rate_2016=gradute_rate[0][0].rate2016;
				g_rate_2015=gradute_rate[0][0].rate2015;
				g_rate_2014=gradute_rate[0][0].rate2014;
				g_rate.push(g_rate_2014,g_rate_2015,g_rate_2016,g_rate_2017);
	
				//招生、在校、毕业人数统计图表
				enrollment(enrollment_17,enrollment_16,enrollment_15,enrollment_14,enrollment_13);
				students(students_17,students_16,students_15,students_14,students_13);
				graduate(graduate_17,graduate_16,graduate_15,graduate_14,graduate_13);
				
				//招生、在校、毕业人数增长率图表
				er(e_rate);
				sr(s_rate);		
				gr(g_rate);
				
				//各年份的高中职毕业生数和专本科招生数图表
				gae2017(gae_2017);		
				gae2016(gae_2016);		
				gae2015(gae_2015);		
				gae2014(gae_2014);
				gae2013(gae_2013);
				
				//各年份的总人口中的在校生占比图表
				sip2017(sip_2017);
				sip2016(sip_2016);
				sip2015(sip_2015);
				sip2014(sip_2014);
				sip2013(sip_2013);
				
			},function(){
				console.log('error');
			});
		};
	
	//切换按钮					
	function toggle(){
			//默认隐藏
			$('#students').hide();
			$('#graduate').hide();
			$('#students_rate').hide();
			$('#graduate_rate').hide();
			$('#gae2016').hide();
			$('#gae2015').hide();
			$('#gae2014').hide();
			$('#gae2013').hide();
			$('#sip2016').hide();
			$('#sip2015').hide();
			$('#sip2014').hide();
			$('#sip2013').hide();
		
			//第一组
			$("button[name='enrollment']").click(function(){
				$('#enrollment').show();
				$('#students').hide();
				$('#graduate').hide();
			});
			$("button[name='students']").click(function(){
				$('#enrollment').hide();
				$('#students').show();
				$('#graduate').hide();
			});
			$("button[name='graduate']").click(function(){
				$('#enrollment').hide();
				$('#students').hide();
				$('#graduate').show();
			});
		
			//第二组
			$("button[name='e_rate']").click(function(){
				$('#enrollment_rate').show();
				$('#students_rate').hide();
				$('#graduate_rate').hide();
			});
			$("button[name='s_rate']").click(function(){
				$('#enrollment_rate').hide();
				$('#students_rate').show();
				$('#graduate_rate').hide();
			});
			$("button[name='g_rate']").click(function(){
				$('#enrollment_rate').hide();
				$('#students_rate').hide();
				$('#graduate_rate').show();
			});
		
			//第三组
			$("button[name='gae_2017']").click(function(){
				$('#gae2017').show();
				$('#gae2016').hide();
				$('#gae2015').hide();
				$('#gae2014').hide();
				$('#gae2013').hide();
			});
			$("button[name='gae_2016']").click(function(){
				$('#gae2016').show();
				$('#gae2017').hide();
				$('#gae2015').hide();
				$('#gae2014').hide();
				$('#gae2013').hide();
			});
			$("button[name='gae_2015']").click(function(){
				$('#gae2015').show();
				$('#gae2016').hide();
				$('#gae2017').hide();
				$('#gae2014').hide();
				$('#gae2013').hide();
			});
			$("button[name='gae_2014']").click(function(){
				$('#gae2014').show();
				$('#gae2016').hide();
				$('#gae2015').hide();
				$('#gae2017').hide();
				$('#gae2013').hide();
			});
			$("button[name='gae_2013']").click(function(){
				$('#gae2013').show();
				$('#gae2016').hide();
				$('#gae2015').hide();
				$('#gae2014').hide();
				$('#gae2017').hide();
			});
		
			//第四组
			$("button[name='sip_2017']").click(function(){
				$('#sip2017').show();
				$('#sip2016').hide();
				$('#sip2015').hide();
				$('#sip2014').hide();
				$('#sip2013').hide();
			});
			$("button[name='sip_2016']").click(function(){
				$('#sip2017').hide();
				$('#sip2016').show();
				$('#sip2015').hide();
				$('#sip2014').hide();
				$('#sip2013').hide();
			});
			$("button[name='sip_2015']").click(function(){
				$('#sip2017').hide();
				$('#sip2016').hide();
				$('#sip2015').show();
				$('#sip2014').hide();
				$('#sip2013').hide();
			});
			$("button[name='sip_2014']").click(function(){
				$('#sip2017').hide();
				$('#sip2016').hide();
				$('#sip2015').hide();
				$('#sip2014').show();
				$('#sip2013').hide();
			});
			$("button[name='sip_2013']").click(function(){
				$('#sip2017').hide();
				$('#sip2016').hide();
				$('#sip2015').hide();
				$('#sip2014').hide();
				$('#sip2013').show();
			});
		};	
	
	//招生、在校、毕业人数统计图表
	function enrollment(enrollment_17,enrollment_16,enrollment_15,enrollment_14,enrollment_13){
		//获取到对应的div
		var charts=echarts.init(document.getElementById('enrollment'));
		//配置选择项
		var options={
			title:{
				text:"招生数",
				},
				tooltip:{
					trigger:'axis',
					axisPointer:{
						type:'shadow',
						formatter:''
					}
				},
				legend:{
					data:['2017年','2016年','2015年','2014年','2013年']
				},
				xAxis:{
					axisPointer:{
						formatter:''
					}
				},
				yAxis:{
					type:'category',
					data:['普通本专科','专科','普通高中','中等职业教育','初中','普通小学']
				},
				series:[{
					name:'2017年',
					type:'bar',
					data:enrollment_17
				},{
					name:'2016年',
					type:'bar',
					data:enrollment_16
				},{
					name:'2015年',
					type:'bar',
					data:enrollment_15
				},{
					name:'2014年',
					type:'bar',
					data:enrollment_14
				},{
					name:'2013年',
					type:'bar',
					data:enrollment_13
				}]
			};
			charts.setOption(options);
		};	
	function students(students_17,students_16,students_15,students_14,students_13){
			var charts=echarts.init(document.getElementById('students'));
			var options={
				title:{
					text:"在校学生数",
				},
				tooltip:{
					trigger:'axis',
					axisPointer:{
						type:'shadow'
					}
				},
				legend:{
					data:['2017年','2016年','2015年','2014年','2013年']
				},
				xAxis:{
					type:'value',
				},
				yAxis:{
					type:'category',
					data:['普通本专科','专科','普通高中','中等职业教育','初中','普通小学']
				},
				series:[{
					name:'2017年',
					type:'bar',
					data:students_17
				},{
					name:'2016年',
					type:'bar',
					data:students_16
				},{
					name:'2015年',
					type:'bar',
					data:students_15
				},{
					name:'2014年',
					type:'bar',
					data:students_14
				},{
					name:'2013年',
					type:'bar',
					data:students_13
				}]
			};
			charts.setOption(options);
		};	
	function graduate(graduate_17,graduate_16,graduate_15,graduate_14,graduate_13){
			var charts=echarts.init(document.getElementById('graduate'));
			var options={
				title:{
					text:"毕业生数",
				},
				tooltip:{
					trigger:'axis',
					axisPointer:{
						type:'shadow'
					}
				},
				legend:{
					data:['2017年','2016年','2015年','2014年','2013年']
				},
				xAxis:{
					type:'value',
				},
				yAxis:{
					type:'category',
					data:['普通本专科','专科','普通高中','中等职业教育','初中','普通小学']
				},
				series:[{
					name:'2017年',
					type:'bar',
					data:graduate_17
				},{
					name:'2016年',
					type:'bar',
					data:graduate_16
				},{
					name:'2015年',
					type:'bar',
					data:graduate_15
				},{
					name:'2014年',
					type:'bar',
					data:graduate_14
				},{
					name:'2013年',
					type:'bar',
					data:graduate_13
				}]
			};
			charts.setOption(options);
		};
	
	//招生、在校、毕业人数增长率图表
	function er(e_rate){
			var charts=echarts.init(document.getElementById('enrollment_rate'));
			var options={
				title:{
					text:"招生增长率",
				},
				tooltip:{
					trigger:'axis',
					formatter:'{c}%'
				},
				legend:{},
				xAxis:{
					type:'category',
					data:['2014年','2015年','2016年','2017年']
				},
				yAxis:{
					axisLabel:{
						formatter:'{value} %'
					}
				},
				series:[{
					type:'line',
					data:e_rate
				}]
			};
			charts.setOption(options);
		};	
	function sr(s_rate){
			var charts=echarts.init(document.getElementById('students_rate'));
			var options={
				title:{
					text:"在校学生增长率",
				},
				tooltip:{
					trigger:'axis',
					formatter:'{c}%'
				},
				legend:{},
				xAxis:{
					type:'category',
					data:['2014年','2015年','2016年','2017年']
				},
				yAxis:{
					axisLabel:{
						formatter:'{value} %'
					}
				},
				series:[{
					type:'line',
					data:s_rate
				}]
			};
			charts.setOption(options);
		};	
	function gr(g_rate){
			var charts=echarts.init(document.getElementById('graduate_rate'));
			var options={
				title:{
					text:"毕业生增长率",
				},
				tooltip:{
					trigger:'axis',
					formatter:'{c}%'
				},
				legend:{},
				xAxis:{
					type:'category',
					data:['2014年','2015年','2016年','2017年']
				},
				yAxis:{
					axisLabel:{
						formatter:'{value} %'
					}
				},
				series:[{
					type:'line',
					data:g_rate
				}]
			};
			charts.setOption(options);
		};			
	
	//各年份的高中职毕业生数和专本科招生数图表
	function gae2017(gae_2017){
		var charts=echarts.init(document.getElementById('gae2017'));
			var options={
				title:{
					text:"2017年高中职毕业生和本专科招生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'高中职毕业生数对比本专科招生数',
					type:'pie',
					data:[
						{value:gae_2017[0][0].graduate,name:"高中职毕业生",itemStyle:{color:"#e03636"}},
						{value:gae_2017[0][0].enrollment,name:'本专科招生数',itemStyle:{color:"#25c6fc"}}
					]
				}]
			};
			charts.setOption(options);
		};
	function gae2016(gae_2016){
		var charts=echarts.init(document.getElementById('gae2016'));
			var options={
				title:{
					text:"2016年高中职毕业生和本专科招生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'高中职毕业生数对比本专科招生数',
					type:'pie',
					data:[
						{value:gae_2016[0][0].graduate,name:"高中职毕业生",itemStyle:{color:"#e03636"}},
						{value:gae_2016[0][0].enrollment,name:'本专科招生数',itemStyle:{color:"#25c6fc"}}
					]
				}]
			};
			charts.setOption(options);
		};
	function gae2015(gae_2015){
		var charts=echarts.init(document.getElementById('gae2015'));
			var options={
				title:{
					text:"2015年高中职毕业生和本专科招生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'高中职毕业生数对比本专科招生数',
					type:'pie',
					data:[
						{value:gae_2015[0][0].graduate,name:"高中职毕业生",itemStyle:{color:"#e03636"}},
						{value:gae_2015[0][0].enrollment,name:'本专科招生数',itemStyle:{color:"#25c6fc"}}
					]
				}]
			};
			charts.setOption(options);
		};			
	function gae2014(gae_2014){
		var charts=echarts.init(document.getElementById('gae2014'));
			var options={
				title:{
					text:"2014年高中职毕业生和本专科招生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'高中职毕业生数对比本专科招生数',
					type:'pie',
					data:[
						{value:gae_2014[0][0].graduate,name:"高中职毕业生",itemStyle:{color:"#e03636"}},
						{value:gae_2014[0][0].enrollment,name:'本专科招生数',itemStyle:{color:"#25c6fc"}}
					]
				}]
			};
			charts.setOption(options);
		};			
	function gae2013(gae_2013){
		var charts=echarts.init(document.getElementById('gae2013'));
			var options={
				title:{
					text:"2013年高中职毕业生和本专科招生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'高中职毕业生数对比本专科招生数',
					type:'pie',
					data:[
						{value:gae_2013[0][0].graduate,name:"高中职毕业生",itemStyle:{color:"#e03636"}},
						{value:gae_2013[0][0].enrollment,name:'本专科招生数',itemStyle:{color:"#25c6fc"}}
					]
				}]
			};
			charts.setOption(options);
		};
	
	//各年份的总人口中的在校生占比图表
	function sip2017(sip_2017){
		var charts=echarts.init(document.getElementById('sip2017'));
			var options={
				title:{
					text:"2017年全国人口中的在校生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'2017年全国人口中的在校生数',
					type:'pie',
					data:[
						{value:sip_2017[0][0].students,name:"全国在校生总数",itemStyle:{color:"#ffc09f"}},
						{value:sip_2017[0][0].peope,name:'全国总人口',itemStyle:{color:"#4cb4e7"}}
					]
				}]
			};
			charts.setOption(options);
		};
	function sip2016(sip_2016){
		var charts=echarts.init(document.getElementById('sip2016'));
			var options={
				title:{
					text:"2016年全国人口中的在校生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'2016年全国人口中的在校生数',
					type:'pie',
					data:[
						{value:sip_2016[0][0].students,name:"全国在校生总数",itemStyle:{color:"#ffc09f"}},
						{value:sip_2016[0][0].peope,name:'全国总人口',itemStyle:{color:"#4cb4e7"}}
					]
				}]
			};
			charts.setOption(options);
		};
	function sip2015(sip_2015){
		var charts=echarts.init(document.getElementById('sip2015'));
			var options={
				title:{
					text:"2015年全国人口中的在校生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'2015年全国人口中的在校生数',
					type:'pie',
					data:[
						{value:sip_2015[0][0].students,name:"全国在校生总数",itemStyle:{color:"#ffc09f"}},
						{value:sip_2015[0][0].peope,name:'全国总人口',itemStyle:{color:"#4cb4e7"}}
					]
				}]
			};
			charts.setOption(options);
		};
	function sip2014(sip_2014){
		var charts=echarts.init(document.getElementById('sip2014'));
			var options={
				title:{
					text:"2014年全国人口中的在校生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'2014年全国人口中的在校生数',
					type:'pie',
					data:[
						{value:sip_2014[0][0].students,name:"全国在校生总数",itemStyle:{color:"#ffc09f"}},
						{value:sip_2014[0][0].peope,name:'全国总人口',itemStyle:{color:"#4cb4e7"}}
					]
				}]
			};
			charts.setOption(options);
		};
	function sip2013(sip_2013){
		var charts=echarts.init(document.getElementById('sip2013'));
			var options={
				title:{
					text:"2013年全国人口中的在校生数",
				},
				tooltip:{
        			formatter: "{a} <br/>{b} : {c}万人 ({d}%)"
				},
				series:[{
					name:'2013年全国人口中的在校生数',
					type:'pie',
					data:[
						{value:sip_2013[0][0].students,name:"全国在校生总数",itemStyle:{color:"#ffc09f"}},
						{value:sip_2013[0][0].peope,name:'全国总人口',itemStyle:{color:"#4cb4e7"}}
					]
				}]
			};
			charts.setOption(options);
		};
	
	return new charts();
})();
						
			
			