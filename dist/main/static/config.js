var config = {
	data:{
		message:"自动功能页面测试",
		show:{
	  			module:"platform",
	  			dataList: [],
	  			fields:[

	  			
	  			],
	  			operation:"",
	  			form_data:{

	  			}
	  	},
	  	getDataURL:"/getTemplte",
	  	saveDataURL:"/saveTemplte",
	  	updateDataURL:"/updateTemplte",
	  	deleteDataURL:"/deleteTemplte",
	  	socketioURL:"http://localhost:8888/collection",
		functions:[

			{
	  			name:"platform",
	  			fields:[
	  					{
	  					showName:"",
	  					name:"service_type",
	  					must_send:false,
	  					must_save:true,
	  					type:"hidden",
	  					placeholder:"",
	  					value:"service_type"
	  					},
		  				{
		  					showName:"",
		  					name:"type",
		  					must_send:false,
		  					must_save:true,
		  					type:"hidden",
		  					placeholder:"",
		  					value:"platform"
		  				},
		  				{
		  					showName:"service",
		  					name:"service",
		  					must_send:true,
		  					must_save:true,
		  					type:"input",
		  					placeholder:"服务访问名称",
		  				},
		  				{
		  					showName:"备注",
		  					name:"backup",
		  					must_send:false,
		  					must_save:false,
		  					type:"input",
		  					placeholder:"",
		  				},
		  				{
		  					showName:"host",
		  					name:"host",
		  					must_send:false,
		  					must_save:true,
		  					type:"input",
		  					placeholder:"数据库ip",
		  				},
		  				{
		  					showName:"user",
		  					name:"user",
		  					must_send:false,
		  					must_save:true,
		  					type:"input",
		  					placeholder:"数据库用户名",
		  				},
		  				{
		  					showName:"password",
		  					name:"password",
		  					must_send:false,
		  					must_save:true,
		  					type:"input",
		  					placeholder:"数据库密码",
		  				},
		  				{
		  					showName:"SQL",
		  					name:"sql",
		  					must_send:false,
		  					must_save:true,
		  					type:"input",
		  					placeholder:"查询sql语句",
		  				},
		  				{
		  					showName:"搜索字段 1",
		  					name:"search_field_1",
		  					must_send:false,
		  					must_save:false,
		  					type:"input",
		  					placeholder:"搜索字段",
		  				},

		  				{
		  					showName:"搜索字段 1 内容",
		  					name:"search_content_1",
		  					must_send:false,
		  					must_save:false,
		  					type:"input",
		  					placeholder:"搜索字段内容",
		  				}
		  				]

	  			},
	  		{
	  			name:"opc",

	  		},
	  		{
	  			name:"rtsp2rtmp"
	  		},
	  		{
	  			name:"sqlserver"
	  		},
	  		{
	  			name:"mysql",

	  		},
	  		{
	  			name:"oracle"
	  		},
	  		{
	  			name:"modbus"
	  		},
	  		{
	  			name:"bacnet"
	  		},
	  		{
	  			name:"avatar"
	  		},
	  		


	  	]	
	}
}


window.$config = config