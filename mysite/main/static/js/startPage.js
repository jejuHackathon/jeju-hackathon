import { getItem, setItem } from './storage.js';

export default function StartPage() {
    const nickNameInput = document.querySelector('.oreum-start__nickname');
    const learnButton = document.querySelector('.oreum-start__learn-button');
    let nickname = '';

    const init = () => {
        nickNameInput?.addEventListener('change', handleOnChangeNickName);
        learnButton?.addEventListener('click', handleOnClickLearnButton);
        nickname = getItem('nickname', '');
        if(nickname) {
            location.href = "/home";
        }
    }

    const handleOnChangeNickName = (e) => {
        nickname = e.target.value;
    }

    const handleOnClickLearnButton = () => {
        if(!nickname) {
            alert('값을 입력해주세요!')
            return;
        }
        setItem('nickname', nickname);
        location.href = "/home";
    }

    init();
}

StartPage();