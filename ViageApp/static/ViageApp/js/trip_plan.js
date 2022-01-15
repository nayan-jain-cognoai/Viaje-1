
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


function save_itinerary_button(){
    let all_divs = document.getElementsByClassName("all_divs")
    let day_trip = {}
    for(let i = 1; i < all_divs.length; i++){
        let daily_budget = all_divs[i].querySelectorAll(".daily_budget")[0].value
        let all_places_inside_all_div = all_divs[i].getElementsByClassName("entire_place");
        let json_trip = {}
        for(let j = 0; j < all_places_inside_all_div.length; j++){
            place_div = all_divs[i].getElementsByClassName("entire_place")[j]
            place = place_div.getElementsByClassName("add_a_place_here")[0].value
            let place_dict = {
                "place": place
            }
            let note_button = place_div.getElementsByClassName("duplicate_note")[0]
            let all_text_notes = place_div.querySelectorAll(".text_note");
            var text_notes = [] 
            for(let k = 0; k < all_text_notes.length; k++){
                text_notes.push(all_text_notes[k].value)
            }
            place_dict["notes"] = text_notes

            all_titles = place_div.querySelectorAll(".list_key");
            all_title_values = place_div.querySelectorAll(".list_value");
            let title_list = []
            for(let m = 0; m < all_titles.length; m++){
                title_list.push({"title":all_titles[m].value,"value":all_title_values[m].value,"index":m})
            }       
            place_dict["title_list"] = title_list


            json_trip[j] = place_dict
        }
        
        day_trip[i] = {"day_trip_details":json_trip, "daily_budget":daily_budget}
    }
    
    const csrftoken = Cookies.get('csrftoken');
    let pk=""
    url_parameters = get_url_vars();
    pk = url_parameters["pk"]
    
    if(typeof pk === "undefined"){
        pk = ""
    }
    console.log(pk)
    let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                "trip":day_trip,
                "pk":pk
            })
        }

    let fetchRes = fetch("/book_trip/", options);
    let response;

    fetchRes.then(res =>
        res.json()).then(response => {
            response = response;
            console.log(response)
            let trip_pk = response["pk"]
            window.location.href = "/edit_trip/?pk="+trip_pk
        })
}