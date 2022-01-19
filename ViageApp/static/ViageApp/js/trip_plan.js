
var day = 0;
var original = document.getElementsByClassName('all_divs')[0];

function duplicate_day() {
    // duplicating and updating id of div
    var clone = original.cloneNode(true);
    clone.style.display = "block";
    // appending
    original.parentNode.appendChild(clone);
    var scrollingElement = (document.scrollingElement || document.body);
    scrollingElement.scrollTop = scrollingElement.scrollHeight;
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
