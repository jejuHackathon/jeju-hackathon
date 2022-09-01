export default function Modal() {
    const okButton = document.querySelector('.modal-ok-button');

    const handleOkClick = () => {
        const $modal = document.querySelector('.modal');
        $modal?.classList.toggle('show');
    }

    const handleEventListener = () => {
        okButton.addEventListener('click', handleOkClick);
    }

    handleEventListener();
}