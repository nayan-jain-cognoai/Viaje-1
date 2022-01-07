window.onload = function(){
            duplicate_day()
        }

var day = 0;
var original = document.getElementById('duplicater');

function duplicate_day() {

      // duplicating and updating id of div
      day = Number(day) + 1
      var total = 1;
      var place = 1;
      var clone = original.cloneNode(true); 

      var day_place_total_str = day + '_place_' + place + '_total_' + total

      clone.id = "duplicater_"+ day_place_total_str;
      clone.setAttribute("day", day);
      clone.setAttribute("place",place);
      clone.setAttribute("total", total);
      clone.style.display = "block";

      // duplicating and updating id of note_button,note,note_div
      note_div_new_id = 'note_div_'+ day + '_place_' + place 
      note_element_new_id = 'note_day_' + day_place_total_str
      note_button_new_id = 'duplicater_add_note_button_day_' + day + '_place_' + place
      place_button_id = 'add_place_button_day_' + day + '_place_' + place + '_total_' + total
      entire_place = 'entire_place_' + day + '_place_' + place + '_total_' + total
      main_place_div = 'main_place_div_' + day
      custom_list = "custom_list_" + day_place_total_str
      custom_list_header_input = "custom_list_header_input_" + day_place_total_str
      custom_list_input = "custom_list_input_" + day_place_total_str
      custom_list_button = "custom_list_button_" + day_place_total_str


      $(clone).find("#note").attr('id',note_element_new_id );
      $(clone).find("#note_div").attr('id',note_div_new_id)
      $(clone).find("#duplicater_add_note_button").attr('id',note_button_new_id)
      $(clone).find("#add_place_button").attr('id',place_button_id)
      $(clone).find("#entire_place").attr('id',entire_place)
      $(clone).find("#main_place_div").attr('id',main_place_div)
      $(clone).find("#custom_list").attr('id',custom_list)
      $(clone).find("#custom_list_header_input").attr('id',custom_list_header_input)
      $(clone).find("#custom_list_input").attr('id',custom_list_input)
      $(clone).find("#custom_list_button").attr('id',custom_list_button)


                  
      // appending
      original.parentNode.appendChild(clone);

      note_button_element = document.getElementById(note_button_new_id)
      note_button_element.setAttribute("day", day);
      note_button_element.setAttribute("place",place);
      note_button_element.setAttribute("total", total);

      note_div_element = document.getElementById(note_div_new_id)
      note_div_element.setAttribute("day", day);
      note_div_element.setAttribute("place",place);
      note_div_element.setAttribute("total", total);


      note_element = document.getElementById(note_element_new_id)
      note_element.setAttribute("day", day);
      note_element.setAttribute("place",place);
      note_element.setAttribute("total", total);

      place_button_element = document.getElementById(place_button_id)
      place_button_element.setAttribute("day", day);
      place_button_element.setAttribute("place", place);
      place_button_element.setAttribute("total", total);


      entire_place_element = document.getElementById(entire_place)
      entire_place_element.setAttribute("day", day);
      entire_place_element.setAttribute("place", place);
      entire_place_element.setAttribute("total", total);

      main_place_element = document.getElementById(main_place_div)
      main_place_element.setAttribute("day", day);


      custom_list = document.getElementById(custom_list)
      custom_list_header_input = document.getElementById(custom_list_header_input)
      custom_list_input = document.getElementById(custom_list_input)
      custom_list_button = document.getElementById(custom_list_button)


      custom_list.setAttribute("day", day);
      custom_list.setAttribute("place", place);
      custom_list.setAttribute("total", total);

      custom_list_header_input.setAttribute("day", day);
      custom_list_header_input.setAttribute("place", place);
      custom_list_header_input.setAttribute("total", total);

      custom_list_input.setAttribute("day", day);
      custom_list_input.setAttribute("place", place);
      custom_list_input.setAttribute("total", total);

      custom_list_button.setAttribute("day", day);
      custom_list_button.setAttribute("place", place);
      custom_list_button.setAttribute("total", total);







      var scrollingElement = (document.scrollingElement || document.body);
      scrollingElement.scrollTop = scrollingElement.scrollHeight;
}



function duplicate_note(elem){
      note_button_element = elem
      day = elem.getAttribute("day")
      place = elem.getAttribute("place")
      total = elem.getAttribute("total")

      var day_place_total_str = day + '_place_' + place + '_total_' + total
      var original = document.getElementById('note_day_'+ day_place_total_str)

      incremental_total = Number(total) + 1
      elem.setAttribute("total",incremental_total)

      var clone = original.cloneNode(true); 
      clone.id = 'note_day_'+ day + '_place_' + place + '_total_' + incremental_total

      // appending
      var item = document.getElementById("note_div_"+ day + '_place_' + place)
      item.setAttribute("total",incremental_total)
      item.appendChild(clone);
      item.appendChild(document.createElement("BR"));
}

function duplicate_place(elem){
      place_button_elem = elem
      day = elem.getAttribute("day")
      place = elem.getAttribute("place")
      total = elem.getAttribute("total")

      var day_place_total_str = day + '_place_' + place + '_total_' + total;
      var original = document.getElementById("entire_place_"+day + '_place_' + place + '_total_' + total);

      place = Number(place) + 1;
      total_for_place = Number(total) + 1
      elem.setAttribute("total",total_for_place);
      elem.setAttribute("place",place)

      var original_to_clone = document.getElementsByClassName("entire_place")[0];

      var clone = original_to_clone.cloneNode(true); 
      button_elem = $(clone).find(".add_place_button")
      daily_budget = $(clone).find(".daily_budget")
      button_elem[0].style.display = "none";
      daily_budget[0].style.display = "none";
      parentNode = document.getElementById("main_place_div_"+ day)
      parentNode.appendChild(clone)



      var day_place_total_str = day + '_place_' + place + '_total_' + 1

      note_button_element = $(clone).find("#duplicater_add_note_button")[0]
      note_button_new_id = 'duplicater_add_note_button_day_' + day + '_place_' + place
      note_button_element.id = note_button_new_id
      note_button_element.setAttribute("day", day);
      note_button_element.setAttribute("place",place);
      note_button_element.setAttribute("total", 1);

      note_div_element = $(clone).find("#note_div")[0]
      note_div_new_id = 'note_div_'+ day + '_place_' + place
      note_div_element.id = note_div_new_id
      note_div_element.setAttribute("day", day);
      note_div_element.setAttribute("place",place);
      note_div_element.setAttribute("total", 1);

      note_element = $(clone).find("#note")[0]
      note_element_new_id = 'note_day_' + day_place_total_str
      note_element.id = note_element_new_id
      note_element.setAttribute("day", day);
      note_element.setAttribute("place",place);
      note_element.setAttribute("total", 1);
}

function duplicate_custom_list(elem){
      var custom_list_to_clone = document.getElementsByClassName("custom_list")[0];
      var clone = custom_list_to_clone.cloneNode(true);

      main_element_button = elem.parentNode
      var id = main_element_button.id
      var day = main_element_button.getAttribute("day")
      var place = main_element_button.getAttribute("place")
      var total = main_element_button.getAttribute("total")

      var day_place_total_str = day + '_place_' + place + '_total_' + total;

      elem.parentNode.parentNode.parentNode.appendChild(clone);
      elem.parentNode.parentNode.parentNode.appendChild(document.createElement("BR"));

      total = Number(total) + 1;
      main_element_button.setAttribute("total",total)
      var day_place_total_str = day + '_place_' + place + '_total_' + total;

      custom_list_header_input = $(clone).find(".custom_list_header_input")[0];
      custom_list_input = $(clone).find(".custom_list_input")[0];
      custom_list_button = $(clone).find(".custom_list_button")[0];      


      custom_list_header_input.id = "custom_list_header_input_" + day_place_total_str
      custom_list_header_input.setAttribute("day", day);
      custom_list_header_input.setAttribute("place", place);
      custom_list_header_input.setAttribute("total", total);


      custom_list_input.id = "custom_list_input_" + day_place_total_str
      custom_list_input.setAttribute("day", day);
      custom_list_input.setAttribute("place", place);
      custom_list_input.setAttribute("total", total);


      custom_list_button.id = "custom_list_button_" + day_place_total_str
      custom_list_button.setAttribute("day", day);
      custom_list_button.setAttribute("place", place);
      custom_list_button.setAttribute("total", total);
      custom_list_button.innerHTML = ""






      
}