
var day = window.day;
var original = document.getElementsByClassName('all_divs')[0];

function duplicate_day(called_on_load=false) {
    // duplicating and updating id of div
    
    if(day >= window.dates_between.length){
        alert("Please extend the dates to proceed");
        return;
    }

    var clone = original.cloneNode(true);
    clone.style.display = "block";
    // appending
    original.parentNode.appendChild(clone);

    if(called_on_load == false){
        var scrollingElement = (document.scrollingElement || document.body);
        scrollingElement.scrollTop = scrollingElement.scrollHeight;
        var dates_between = window.dates_between
    }
    
    
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    var date_to_show = dates_between[day].toLocaleDateString("en-US", options);
    var date_to_show_in_calendar = dates_between[day].toLocaleDateString("en-US");
    clone.getElementsByClassName("date_of_trip")[0].innerHTML = date_to_show
    clone.getElementsByClassName("date_in_calendar")[0].innerHTML = ` <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="calendar-alt" class="svg-inline--fa fa-calendar-alt fa-w-14 fa-fw mr-2" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                            <path fill="currentColor" d="M148 288h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm108-12v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm96 0v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm-96 96v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm-96 0v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm192 0v-40c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm96-260v352c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V112c0-26.5 21.5-48 48-48h48V12c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v52h128V12c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v52h48c26.5 0 48 21.5 48 48zm-48 346V160H48v298c0 3.3 2.7 6 6 6h340c3.3 0 6-2.7 6-6z"></path>
                        </svg>
                         ` + ` ` + date_to_show_in_calendar
    // clone.getElementsByClassName("date_in_calendar")[0].innerHTML = date_to_show_in_calendar
    day = day + 1;
}

function duplicate_note(elem) {
    let note_button_element = elem
    let parent_div = note_button_element.parentNode.parentNode.parentNode.querySelectorAll(".note_div")[0]
    let original = document.getElementsByClassName('note_input')[0]
    
    let clone = original.cloneNode(true);
    clone.querySelectorAll(".remove_icon_notes")[0].style.display = "";
    // appending
    parent_div.appendChild(clone);
}

function duplicate_place(elem) {
    place_button_elem = elem
    var original_to_clone = document.getElementsByClassName("entire_place")[0];
    var clone = original_to_clone.cloneNode(true);
    clone.querySelectorAll(".daily_budget")[0].style.display = "none";
    clone.querySelectorAll(".add_place_button")[0].style.display = "none";
    clone.querySelectorAll(".remove_icon_place")[0].style.display = "";
    let parent_div = place_button_elem.parentNode.parentNode.parentNode.parentNode
    
    parent_div.appendChild(clone)

}

function duplicate_custom_list(elem) {
    var custom_list_to_clone = document.getElementsByClassName("custom_list")[0];
    var clone = custom_list_to_clone.cloneNode(true);
    clone.querySelectorAll(".custom_list_button")[0].innerHTML = `<i class="remove_icon_list fa fa-remove" style="font-size:30px;color:red;padding: 3px;cursor: pointer;" onclick="remove_icon_list(this)"></i>`;
    
    main_element_button = elem.parentNode
    elem.parentNode.parentNode.parentNode.appendChild(clone);
    
}

function remove_icon_place(elem){
    elem.parentNode.parentNode.parentNode.remove();
}

function remove_icon_notes(elem){
    elem.parentNode.remove();
}

function remove_icon_list(elem){
    elem.parentNode.parentNode.remove();
}

function get_url_vars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m, key, value) {
        vars[key] = value;
    });
    return vars;
}

