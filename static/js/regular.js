/**
 * Created by liuwenwu on 2018/5/7.
 */
//========正则检验

//-------获得显示信息的盒子
var showInfo = document.querySelector('.showInfo');

showInfo.style.display = "none";

//--------user
function user(value){
    var check = new Check(value);
    var user = document.querySelector('.user');
    if (!check.username(value)){
        showInfo.style.display = "block";
        showInfo.innerHTML = "您的用户名格式输入有误,请重新输入";
        user.style.borderColor = "red";
    }else{
        showInfo.style.display = "none";
        user.style.borderColor = "green";
    }
}

//---------密码
function pass(value){
    var check = new Check(value);
    var pass = document.querySelector(".pass");
    if (!check.password(value)){
        showInfo.style.display = "block";
        showInfo.innerHTML = "您的密码格式输入有误,请重新输入";

        pass.style.borderColor = "red";
    }else{
        showInfo.style.display = "none";
        pass.style.borderColor = "green";
    }
}

//--------邮箱
function emails(value){
    var check = new Check(value);
    var email = document.querySelector(".email");
    if (!check.email(value)){
        showInfo.style.display = "block";
        showInfo.innerHTML = "您的密码格式输入有误,请重新输入";

        pass.style.borderColor = "red";
    }else{
        showInfo.style.display = "none";
        pass.style.borderColor = "green";
    }
}

//------电话
function tele(value){
    var check = new Check(value);
    var tele = document.querySelector(".tele");
    if (!check.telephone(value)){
        showInfo.style.display = "block";
        showInfo.innerHTML = "您的电话格式输入有误,请重新输入";

        pass.style.borderColor = "red";
    }else{
        showInfo.style.display = "none";
        pass.style.borderColor = "green";
    }
}


//自响应实现不同分辨率高度
var main = document.querySelector('.main');
main.style.height = window.screen.height;