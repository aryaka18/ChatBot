// frontend/src/utils/api.js
const API_URL = 'http://localhost:5000';

export const sendMessage = async (message) => {
    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: message })
        });
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
};
