/**
 * Created by liuwenwu on 2018/5/7.
 */
function Check(value){
    this.value = value;
}

Check.prototype.rt = function (check) {
    if (check.test(this.value) === true){
        return 1;
    }else{
        return 0;
    }
}
Check.prototype.email = function(){
    var email = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    return this.rt(email);
}

//用户名正则，4到16位（字母，数字，下划线，减号）
Check.prototype.username = function () {
    var username = /^[a-zA-Z0-9_-]{4,16}$/;
    return this.rt(username);
}
//密码强度正则，最少6位，包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符
Check.prototype.password = function () {
    var passwrod = /^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$/;
    return this.rt(passwrod);
}

Check.prototype.telephone = function () {
    var tele = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    return this.rt(tele);
}

