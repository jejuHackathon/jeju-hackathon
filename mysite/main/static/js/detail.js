export default function Detail() {
    const handleButtonClick = (e) => {
        const $button = e.target.closest('button');
        if($button) {
            const className = $button.className;
            const $modal = document.querySelector('.modal');
            const $modalContent = document.querySelector('.modal-content');
            const id = e.target.dataset.id;
            if(className === 'oreum__button--modify') {
                // modify page로 리다이렉트 시키기.
                $modalContent.innerHTML = `서비스 준비중..`;
            } else if(className === 'oreum__button--delete') {
                $modalContent.innerHTML = `${e.target.value}을 삭제하시겠습니까?`;
            }
            $modal.classList.toggle('show');
        }
    }
    
    document.querySelector('.oreum__button').addEventListener('click', handleButtonClick);
}