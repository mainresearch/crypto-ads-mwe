const image_ids =[
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
];

const image_paths =[
    '0.jpg',
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg',
    '8.jpg',
    '9.jpg'
];

let loaded_image_ids;
let loaded_image_paths;
let user_id;


function load_page (){
    console.log ('Loading Page');

    user_id = $('#user_ids').val();

    console.log (`User: ${user_id}`);

    refresh_images ();
}

async function refresh_images (){
    console.log ('Refreshing Images');

    loaded_image_ids = [];
    loaded_image_paths = [];

    $('.main_left').empty();

    for (let i=0; i<image_paths.length; i++){
        if (Math.floor(Math.random() * 3) === 0 || i === 0){
            $('.main_left').append ($('<img>').prop({
                'src': `../img/${i}.jpg`
            }));

            loaded_image_ids.push (i);
            loaded_image_paths.push (`${i}.jpg`);
        }
    }

    if ($('#on_viewing').is(":checked")){
        console.log (`POST 127.0.0.1/general/view_ad/${user_id}/0`);

        try
        {
            data = await $.ajax({
                type: 'POST',
                url: `http://localhost:12345/general/view_ad/${user_id}/0`,
                datatype: 'json',
                contentType: 'application/json; charset=utf-8'
            });

            update_inputs (data);
        }

        catch (e)
        {
            console.log (e);
        }
        console.log (data);
    }
    else{
        console.log ('Payout on ad viewing disabled');
    }
}

async function click_ad (){
    console.log ('Ad clicked');

    if ($('#on_clicking').is(":checked")){
        let data;

        console.log (`POST 127.0.0.1/general/click_ad/${user_id}/0`);

        try
        {
            data = await $.ajax({
                type: 'POST',
                url: `http://localhost:12345/general/click_ad/${user_id}/0`,
                datatype: 'json',
                contentType: 'application/json; charset=utf-8'
            });

            update_inputs (data);
        }

        catch (e)
        {
            console.log (e);
        }
        console.log (data);
    }
    else{
        console.log ('Payout on ad clicking disabled');
    }
}

function change_user (){
    user_id = $('#user_ids').val();

    console.log (`New user: ${user_id}`);

    refresh_images ();
}

function update_inputs (data){
    let revenue;
    let i,j;

    for (i=0;i<10;i++){
        revenue=0.0;
        for (j=0; j<data.user_transactions[i].length;j++){
            revenue+=data.user_transactions[i][j]['amount']
        }
        $(`#user_${i}_revenue`).val(revenue);
    }

    revenue=0.0;
    for (j=0; j<data.server_transactions.length;j++){
        revenue+=data.server_transactions[j]['amount']
    }
    $('#website_revenue').val(revenue);
}
