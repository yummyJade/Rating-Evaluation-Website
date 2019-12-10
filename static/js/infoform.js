
/**
 * @author:jade
 */
/*
type 1代表单选题 
type 2代表判断题
*/ 
let questionSum = 100;
let nowProgess = 20;
var questions = [
    {
        index:'1',
        type:'2',
        title:"你猜啊啊啊啊啊",
        
        options:[
            
               "你说你说"
            ,
            
                "我说我说"
            
        ]
        
    }
]


$(".progress").css({
    'width':'50%'
})



//用于初始化问题等等操作
function dataIn(){
    let str = "",
    strInside = ""
    ;
    $(".questionWrap").children().remove();
    for(let i = 0, len = questions.length; i < len; i++ ){
        strInside = "";

        for(let j = 0, lenInside = questions[i].options.length; j < lenInside; j++ ){
            // console.log(questions[i].options[j])
            strInside +=`
                <li class="questionInfo">${questions[i].options[j]}</li>
            `
        }

        str += `
                <div class="question">
                    <div class="questionTitle">
                        <strong>${"第" + (i+1) + "题"}</strong>
                        ${questions[i].title}
                    </div>
                    
                    <ul>
                        `+ strInside + `
                    </ul>
            </div>
        `
        
        
        // $(".question ul").append(strInside);


    }
    $(".questionWrap").append(str);
}
// dataIn();
//解析
function GetRequest() {   
   var url = location.search; //获取url中"?"符后的字串   
   var theRequest = new Object();   
   if (url.indexOf("?") != -1) {   
      var str = url.substr(1);   
      strs = str.split("&");   
      for(var i = 0; i < strs.length; i ++) {   
         theRequest[strs[i].split("=")[0]]=unescape(strs[i].split("=")[1]);   
      }   
   }   
   return theRequest;   
}    


//数据初始化
function init(){
    // console.log("ssss")
    let type = GetRequest();
    console.log(type.type);
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/jobEval/evaluate/getNaire",
        data: {
            'type':type.type

        },
        dataType: "json",
        success: function(data){
            if(data.status == 1){

            //要修改一下
            $(".input").val(data.type);
            
            let str = "",
            strInside = ""
            ;
            questions = data.data;
            $(".questionWrap").children().remove();
            for(let i = 0, len = questions.length; i < len; i++ ){
                strInside = "";
                //如果是第二种情况那么直接就是是否否
                if(data.type == 2){
                    // for(let j = 0, lenInside = questions[i].options.length; j < lenInside; j++ ){
                        strInside +=`
                                <li class="questionInfo">
                                    <input type="radio" value="${questions[i].options["val1"]}" name="${i}">
                                    是
                                </li>
                                <li class="questionInfo">
                                    <input type="radio" value="${questions[i].options["val2"]}" name="${i}">
                                    否
                                </li>
                            `
                    // }
                }else if(data.type == 1){
                    for(let j = 0, lenInside = questions[i].options.length; j < lenInside; j++ ){
                        // console.log(questions[i].options[j])
                        strInside +=`
                            <li class="questionInfo">
                                <input type="radio" value="${j+1}" name="${i}">
                                ${questions[i].options[j]}
                            </li>
                        `
                    }
                }else if(data.type == 3){
                    strInside +=`
                                <li class="questionInfo">
                                    <input type="radio" value="1" name="${i}">
                                    不太赞同
                                </li>
                                <li class="questionInfo">
                                    <input type="radio" value="2" name="${i}">
                                    一般
                                </li>
                                 <li class="questionInfo">
                                    <input type="radio" value="3" name="${i}">
                                    赞同
                                </li>
                                 <li class="questionInfo">
                                    <input type="radio" value="4" name="${i}">
                                    很赞同
                                </li>
                                 <li class="questionInfo">
                                    <input type="radio" value="5" name="${i}">
                                    非常赞同
                                </li>
                            `
                }
                
        
                str += `
                        <div class="question">
                            <div class="questionTitle">
                                <strong>${"第" + (i+1) + "题"}</strong>
                                ${questions[i].title}
                            </div>
                            
                            <ul>
                                `+ strInside + `
                            </ul>
                    </div>
                `
                
                
                // $(".question ul").append(strInside);
        
        
            }
            $(".questionWrap").append(str);  
         }
        }
    });
}

// $(".submitBtn").click({

//     return false;
// })

$("form").submit(function(){
    // return false;
})

// $(".submitBtn").click(function(){
//     //提交表单


// })
init();
