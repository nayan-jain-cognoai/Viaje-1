 window.onload = function() {
      var sp = new SuperPlaceholder({
        placeholders: ["Paris", "Shillong"],
        preText: "Where to? ",
        stay: 1000,
        speed: 100,
        element: '#dynamic-placeholder'
      });
      sp.init();
    }

    var bindDateRangeValidation = function (f, s, e) {
    if(!(f instanceof jQuery)){
      console.log("Not passing a jQuery object");
    }
  
    var jqForm = f,
        startDateId = s,
        endDateId = e;
  
    var checkDateRange = function (startDate, endDate) {
        var isValid = (startDate != "" && endDate != "") ? startDate <= endDate : true;
        return isValid;
    }

    var bindValidator = function () {
        var bstpValidate = jqForm.data('bootstrapValidator');
        var validateFields = {
            startDate: {
                validators: {
                    notEmpty: { message: 'This field is required.' },
                    callback: {
                        message: 'Start Date must less than or equal to End Date.',
                        callback: function (startDate, validator, $field) {
                            return checkDateRange(startDate, $('#' + endDateId).val())
                        }
                    }
                }
            },
            endDate: {
                validators: {
                    notEmpty: { message: 'This field is required.' },
                    callback: {
                        message: 'End Date must greater than or equal to Start Date.',
                        callback: function (endDate, validator, $field) {
                            return checkDateRange($('#' + startDateId).val(), endDate);
                        }
                    }
                }
            },
            customize: {
                validators: {
                    customize: { message: 'customize.' }
                }
            }
        }
        if (!bstpValidate) {
            jqForm.bootstrapValidator({
                excluded: [':disabled'], 
            })
        }
      
        jqForm.bootstrapValidator('addField', startDateId, validateFields.startDate);
        jqForm.bootstrapValidator('addField', endDateId, validateFields.endDate);
      
    };

    var hookValidatorEvt = function () {
        var dateBlur = function (e, bundleDateId, action) {
            jqForm.bootstrapValidator('revalidateField', e.target.id);
        }

        $('#' + startDateId).on("dp.change dp.update blur", function (e) {
            $('#' + endDateId).data("DateTimePicker").setMinDate(e.date);
            dateBlur(e, endDateId);
        });

        $('#' + endDateId).on("dp.change dp.update blur", function (e) {
            $('#' + startDateId).data("DateTimePicker").setMaxDate(e.date);
            dateBlur(e, startDateId);
        });
    }

    bindValidator();
    hookValidatorEvt();
};


$(function () {
    var sd = new Date(), ed = new Date();
    try{
      $('#startDate').datetimepicker({ 
      pickTime: false, 
      format: "YYYY/MM/DD", 
      defaultDate: sd, 
      //maxDate: ed 
    });
  
    $('#endDate').datetimepicker({ 
      pickTime: false, 
      format: "YYYY/MM/DD", 
      defaultDate: ed, 
      minDate: sd 
    });
    }catch(err){}
    bindDateRangeValidation($("#form"), 'startDate', 'endDate');
});




    var SuperPlaceholder = function(options) {  
  this.options = options;
  this.element = options.element
  this.placeholderIdx = 0;
  this.charIdx = 0;
  

  this.setPlaceholder = function() {
      placeholder = options.placeholders[this.placeholderIdx];
      var placeholderChunk = placeholder.substring(0, this.charIdx+1);
      document.querySelector(this.element).setAttribute("placeholder", this.options.preText + " " + placeholderChunk)
  };
  
  this.onTickReverse = function(afterReverse) {
    if (this.charIdx === 0) {
      afterReverse.bind(this)();
      clearInterval(this.intervalId); 
      this.init(); 
    } else {
      this.setPlaceholder();
      this.charIdx--;
    }
  };
  
  this.goReverse = function() {
      clearInterval(this.intervalId);
      this.intervalId = setInterval(this.onTickReverse.bind(this, function() {
        this.charIdx = 0;
        this.placeholderIdx++;
        if (this.placeholderIdx === options.placeholders.length) {
          // end of all placeholders reached
          this.placeholderIdx = 0;
        }
      }), this.options.speed)
  };
  
  this.onTick = function() {
      var placeholder = options.placeholders[this.placeholderIdx];
      if (this.charIdx === placeholder.length) {
        // end of a placeholder sentence reached
        setTimeout(this.goReverse.bind(this), this.options.stay);
      }
      
      this.setPlaceholder();
    
      this.charIdx++;
    }
  
  this.init = function() {
    this.intervalId = setInterval(this.onTick.bind(this), this.options.speed);
  }
  
  this.kill = function() {
    clearInterval(this.intervalId); 
  }
}


function sign_up_user(){
    const csrftoken = Cookies.get('csrftoken');

    let full_name =  document.getElementById("full_name").value;
    let email_address = document.getElementById("email_address").value;
    let password = document.getElementById("password_one").value;
    let re_enter_password = document.getElementById("password_two").value;

    console.log(password)
    console.log(re_enter_password)
    if(password != re_enter_password){
        alert("Please check the password");
    }



    let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                "full_name":full_name,
                "email_address":email_address,
                "password":password,
                "re_enter_password":re_enter_password
            })
        }

    let fetchRes = fetch("/signup/", options);
    let response;

    fetchRes.then(res =>
        res.json()).then(response => {
            response = response;
            console.log(response)
            
        })
}


function login(){
  const csrftoken = Cookies.get('csrftoken');
  let email_address = document.getElementById("login_email").value;
  let password = document.getElementById("login_password").value;
  let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                "email_address":email_address,
                "password":password,
            })
        }

  let fetchRes = fetch("/login/", options);
  let response;

  fetchRes.then(res =>
      res.json()).then(response => {
          response = response;
          console.log(response)
          
      })
}


const getDatesBetweenDates = (startDate, endDate) => {
          let dates = []
          //to avoid modifying the original date
          const theDate = new Date(startDate)
          while (theDate <= endDate) {
            dates = [...dates, new Date(theDate)]
            theDate.setDate(theDate.getDate() + 1)
          }

          return dates
        }
