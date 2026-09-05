AOS.init();

function togglePassword(){
  console.log("clicked effect");
  let login = document.getElementById('loginpassword');
  let span = document.querySelector('.show-pass-btn');


  if (login.type === "password"){
      login.type = "text";
      span.innerHTML = `<i class="fa-regular fa-eye"></i>`
      
  }
  else{
      login.type = "password";
       span.innerHTML = `<i class="fa-regular fa-eye-slash"></i>`
      
  }

}
