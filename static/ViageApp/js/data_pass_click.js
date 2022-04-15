function create_day_trip_json() {
    let all_divs = document.getElementsByClassName("all_divs")
    let day_trip = {}
    for (let i = 1; i < all_divs.length; i++) {
        let daily_budget = all_divs[i].querySelectorAll(".daily_budget")[0].value
        let date = new Date(all_divs[i].querySelectorAll(".date_of_trip")[0].innerHTML)
        var date_options = {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        };
        var date_to_show = date.toLocaleDateString("en-US", date_options);
        var date_to_show_in_calendar = date.toLocaleDateString("en-US");

        let all_places_inside_all_div = all_divs[i].getElementsByClassName("entire_place");
        let json_trip = {}
        for (let j = 0; j < all_places_inside_all_div.length; j++) {
            place_div = all_divs[i].getElementsByClassName("entire_place")[j]
            place = place_div.getElementsByClassName("add_a_place_here")[0].value
            let place_dict = {
                "place": place
            }
            let note_button = place_div.getElementsByClassName("duplicate_note")[0]
            let all_text_notes = place_div.querySelectorAll(".text_note");
            var text_notes = []
            for (let k = 0; k < all_text_notes.length; k++) {
                text_notes.push(all_text_notes[k].value)
            }
            place_dict["notes"] = text_notes

            all_titles = place_div.querySelectorAll(".list_key");
            all_title_values = place_div.querySelectorAll(".list_value");
            let title_list = []
            for (let m = 0; m < all_titles.length; m++) {
                title_list.push({
                    "title": all_titles[m].value,
                    "value": all_title_values[m].value,
                    "index": m
                })
            }
            place_dict["title_list"] = title_list
            json_trip[j] = place_dict
        }

        day_trip[i] = {
            "day_trip_details": json_trip,
            "daily_budget": daily_budget,
            "date": date,
            "date_to_show": date_to_show,
            "date_to_show_in_calendar": date_to_show_in_calendar
        }

    }

    return day_trip;
}


function day_trip_api_call(day_trip, start_date, end_date, user_pk, important_things_for_trip, start_budget, end_budget) {
    const csrftoken = Cookies.get('csrftoken');

    let url_parameters = get_url_vars();
    let place_to_visit = url_parameters["place_to_visit"];

    let pk = url_parameters["pk"];
    if (typeof pk === "undefined") {
        pk = ""
    }

    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            "trip": day_trip,
            "pk": pk,
            "user_pk": user_pk,
            "important_things_for_trip": important_things_for_trip,
            "start_budget":start_budget,
            "end_budget":end_budget
        })
    }

    let fetchRes = fetch("/book_trip/", options);
    let response;

    fetchRes.then(res =>
        res.json()).then(response => {
        response = response;
        console.log(response)
        let trip_pk = response["pk"]
        window.location.href = "/edit_trip/?pk=" + trip_pk + "&place_to_visit=" + place_to_visit + "&start_date=" + start_date + "&end_date=" + end_date;
    })
}


function save_itinerary_button(user_pk) {
    let day_trip = create_day_trip_json();
    let url_parameters = get_url_vars();
    let start_date = url_parameters["start_date"];
    let end_date = url_parameters["end_date"];
    let start_budget = document.getElementById("from_budget").value
    let end_budget = document.getElementById("to_budget").value

    try {
        editor.save().then((outputData) => {
            console.log('Article data: ', JSON.stringify(outputData))
            day_trip_api_call(day_trip, start_date, end_date, user_pk, JSON.stringify(outputData), start_budget, end_budget);
        }).catch((error) => {
            console.log('Saving failed: ', error)
        });
    } catch (err) {
        console.log(err);
    }



}

function submit_trip_details(is_mobile) {
    if(is_mobile == true){
        var place_to_visit = document.getElementById("dynamic-placeholder-mobile").value
    }else{
        var place_to_visit = document.getElementById("dynamic-placeholder").value
    }
    console.log(place_to_visit);
    let start_date = document.getElementById("startDate").value
    let end_date = document.getElementById("endDate").value
    window.location.href = "/home/?place_to_visit=" + place_to_visit + "&start_date=" + start_date + "&end_date=" + end_date;
}

function custom_sort(a, b) {
    return new Date(a.date).getTime() - new Date(b.date).getTime();
}

function update_dates() {
    let start_date = window.start_date;
    let end_date = window.end_date;

    let start_date_selected = document.getElementById("trip_start").value;
    let end_date_selected = document.getElementById("trip_end").value;

    let day_trip = create_day_trip_json();

    if (start_date_selected < start_date) {
        var date_between_dates = getDatesBetweenDates(start_date_selected, new Date(start_date));
        //console.log(date_between_dates)
        //console.log("here")
        for (var i = 0; i < date_between_dates.length; i++) {
            let date = date_between_dates[i]
            var date_options = {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            };
            var date_to_show = date.toLocaleDateString("en-US", date_options);
            var date_to_show_in_calendar = date.toLocaleDateString("en-US");
            day_trip[i] = {
                "date": date,
                "daily_budget": "",
                "date_to_show": date_to_show,
                "day_trip_details": {
                    "0": {
                        "notes": [""],
                        "place": "",
                        "title_list": [{
                            "index": 0,
                            "title": "",
                            "value": ""
                        }]
                    }
                },
                "date_to_show_in_calendar": date_to_show_in_calendar
            }
        }

        let object = day_trip
        let trip_array = Object.keys(object).map(function(k) {
            return object[k];
        });

        trip_array.sort(custom_sort);
        day_trip_final_dictionary = {}
        for (let i = 0; i <= trip_array.length; i++) {
            day_trip_final_dictionary[i] = trip_array[i]
        }
    } else if (end_date_selected > end_date) {
        var date_between_dates = getDatesBetweenDates(end_date_selected, new Date(end_date));
        day_trip_final_dictionary = day_trip;
    }


    day_trip_api_call(day_trip_final_dictionary, start_date_selected, end_date_selected)

}


function create_itinerary() {
    let url_parameters = get_url_vars();
    let place_to_visit = url_parameters["place_to_visit"];
    let start_date = url_parameters["start_date"];
    let end_date = url_parameters["end_date"];
    window.location.href = "/trip_plan/?place_to_visit=" + place_to_visit + "&start_date=" + start_date + "&end_date=" + end_date;
}
