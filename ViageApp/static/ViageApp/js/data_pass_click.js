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
    
    let url_parameters = get_url_vars();
    let place_to_visit = url_parameters["place_to_visit"];
    let start_date = url_parameters["start_date"];
    let end_date = url_parameters["end_date"];
    
    let pk = url_parameters["pk"];
    if(typeof pk === "undefined"){
        pk = ""
    }
    
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
            window.location.href = "/edit_trip/?pk="+trip_pk+"&place_to_visit="+place_to_visit+"&start_date="+start_date+"&end_date="+end_date;
        })
}



function submit_trip_details(){
    let place_to_visit = document.getElementById("dynamic-placeholder").value
    let start_date = document.getElementById("startDate").value
    let end_date = document.getElementById("endDate").value
    window.location.href = "/trip_plan/?place_to_visit="+place_to_visit+"&start_date="+start_date+"&end_date="+end_date;

}