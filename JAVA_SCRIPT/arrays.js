// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array



function addNew()
{
  var name = prompt("What name would you like to add?")
  roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster


function remove()
{
  var name = prompt("What name would you like to remove?")
  roster.splice(roster.indexof(name),1)
}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.
function display()
{
  return roster
}


var start = prompt("Would you like to start the roster web app? y/n");
var request = "empty";

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (start === "y") {
  while (request !== "quit") {
    request = prompt("Please select an action: add, remove, display, or quit.")
    if (request === "add") {
      addNew();
    }else if (request === "display") {
      display();
    }else if (request === "remove") {
      remove();
    }
  }
}
alert("Thanks for using the Web App! Please refresh the page to start over.")
