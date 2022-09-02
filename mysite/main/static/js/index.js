import Detail from "./detail.js";
import Modal from './modal.js';
import { getItem } from './storage.js';

const init = () => {
    const route = () => {
        const { pathname } = location;
        if(pathname !== '/') {
            const nickname = getItem('nickname', '');
            if(!nickname) {
                console.log(nickname);
                location.href = "/";
            }
        }
    }

    new Modal();
    new Detail();
    route();
}

init();