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
            if(response["status_code"] == "200"){
            console.log("here")
            alert("Succesfully Signed in, please login.")
            // setTimeout(function(){
            //   window.location.reload()
            // },1000)
          }else{
            alert("System is facing some error")
          }

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
          if(response["status_code"] == "200"){
            console.log("here")
            alert("Succesfully Logged In")
            setTimeout(function(){
              window.location.reload()
            },1000)
          }else{
            alert("Please check your credentials")
          }
      })
}


function logout(){
  let fetchRes = fetch("/logout/");
  let response;

  fetchRes.then(res =>
      res.json()).then(response => {
          response = response;
          console.log(response)
          if(response["status_code"] == "200"){
            console.log("here")
            alert("Succesfully Logged Out")
            setTimeout(function(){
              window.location.reload()
            },1000)
          }else{
            alert("System is facing some error")
          }
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