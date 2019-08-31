var headOne = document.querySelector("#one")
var headTwo = document.querySelector("#two")
var headThree = document.querySelector("#three")

console.log("Its Connected")


headOne.addEventListener("mouseover",function(){
  headOne.textContent = "MOUSE HOVERED"
  headOne.style.color="red"
})

headOne.addEventListener("mouseout",function(){
  headOne.textContent = "MOUSE HOVER ME"
  headOne.style.color="black"
})

headTwo.addEventListener("click",function(){
  headTwo.textContent = "CLICKED"
  headTwo.style.color = "red"
})


headTwo.addEventListener("mouseout",function(){
  headTwo.textContent = "CLICK ME"
  headTwo.style.color="black"
})



headThree.addEventListener("dblclick",function(){
  headThree.textContent = "DOUBLE CLICKED"
  headThree.style.color = "red"
})


headThree.addEventListener("mouseout",function(){
  headThree.textContent = "DOUBLE CLICK ME"
  headThree.style.color="black"
})
