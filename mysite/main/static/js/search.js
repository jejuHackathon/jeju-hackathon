let cityNo = document.querySelectorAll('.j_map');

let toggle = false;
let mapController = false;

cityNo.forEach((item) => {
    // let check = false; 

    item.addEventListener('mouseover', () => {
        if(!toggle) { 
            document.getElementById('city_name').setAttribute(
                'value', item.getAttribute('data-name'));
        }
    });
    
    item.addEventListener('mouseout', () => {
        if(!mapController) {
            document.getElementById('city_name').setAttribute('value', '지역을 선택해주세요');
        }
    })
    
    let cityCheck = '';
    let cityChoice = document.querySelector('.map_controller');

    item.addEventListener('click', () => {
        if(!toggle) {
            cityCheck = item.getAttribute('data-name');
            toggle = true; 
            
            cityChoice.setAttribute('style', 'z-index: 2');
            mapController = true;
            
            item.setAttribute('style', 'fill: #ccffa7');
            

        }
    })
    
    cityChoice.addEventListener('click', () => {
        cityChoice.setAttribute('style', 'z-index: -1');
        item.removeAttribute('style');
        toggle = false;
        mapController = false;
    })

})

function searchBtn() {
    if(document.getElementById('city_name').value == "지역을 선택해주세요") {
        alert('지역을 선택해주세요');
    }
}