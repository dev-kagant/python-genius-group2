import React, { useState } from "react";

import { Modal } from "../../Modal/Modal";
import EditUserForm from "./EditUserForm";

const EditUserModal = ({ setShowForm }) => {
    const [showModal, setShowModal] = useState(true);

    const closeModal = () => {
        setShowModal(false);
        setShowForm(false);
    }

    return (
        <>
            {showModal && (
                <Modal onClose={closeModal}>
                    <EditUserForm closeModal={closeModal}/> 
                </Modal>
            )}
        </>
    )
}

export default EditUserModal;