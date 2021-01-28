import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { Modal } from "../../Modal/Modal";
import SignUpForm from "./SignUpForm";

const LoginModal = () => {
    const history = useHistory();

    const [showModal, setShowModal] = useState(true);

    const closeModal = () => {
        setShowModal(false);
        history.push("/")
    }

    return (
        <>
            {showModal && (
                <Modal onClose={closeModal}>
                    <SignUpForm />
                </Modal>
            )}
        </>
    )
}

export default LoginModal;