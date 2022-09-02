import { getItem, setItem } from './storage.js';

export default function StartPage() {
    const nickNameInput = document.querySelector('.oreum-start__nickname');
    const learnButton = document.querySelector('.oreum-start__learn-button');
    let nickName = '';

    const init = () => {
        nickNameInput?.addEventListener('change', handleOnChangeNickName);
        learnButton?.addEventListener('click', handleOnClickLearnButton);
        nickName = getItem('nickName', '');
        if(nickName) {
            location.href = "/home";
        }
    }

    const handleOnChangeNickName = (e) => {
        nickName = e.target.value;
    }

    const handleOnClickLearnButton = () => {
        if(!nickName) {
            alert('값을 입력해주세요!')
            return;
        }
        setItem('nickName', nickName);
        location.href = "/home";
    }

    init();
}

StartPage();