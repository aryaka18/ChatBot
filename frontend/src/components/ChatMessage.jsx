import React, { useState } from 'react';

const ChatMessage = ({ message, sender, image }) => {
  const [isImageModalOpen, setIsImageModalOpen] = useState(false);

  const renderContent = () => {
    const textContent = <p className="break-words text-sm md:text-base">{message}</p>;
    
    if (image) {
      return (
        <div className="message-content">
          {textContent}
          <div className="mt-4">
            <img
              src={image.url}
              alt={image.alt || "Chat image"}
              className="max-w-full rounded-lg shadow-sm cursor-pointer transition-transform hover:scale-105"
              style={{ maxHeight: "300px" }}
              onClick={() => setIsImageModalOpen(true)}
            />
            {image.caption && (
              <p className="mt-2 text-sm text-gray-600">{image.caption}</p>
            )}
          </div>
        </div>
      );
    }
    
    return textContent;
  };

  return (
    <>
      <div className={`flex ${sender === "user" ? "justify-end" : "justify-start"} p-2`}>
        <div
          className={`p-4 rounded-2xl max-w-[80%] animate-fade-in ${
            sender === "user"
              ? "bg-gradient-to-r from-blue-500 to-purple-500 text-white"
              : "bg-white shadow-md text-gray-800"
          }`}
        >
          {renderContent()}
        </div>
      </div>

      {/* Image Modal */}
      {isImageModalOpen && image && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4"
          onClick={() => setIsImageModalOpen(false)}
        >
          <div className="relative max-w-4xl max-h-[90vh] overflow-auto">
            <img
              src={image.url}
              alt={image.alt || "Chat image"}
              className="max-w-full h-auto rounded-lg"
            />
            {image.caption && (
              <p className="mt-2 text-sm text-white text-center">{image.caption}</p>
            )}
            <button
              className="absolute top-2 right-2 bg-white rounded-full p-2 hover:bg-gray-100"
              onClick={() => setIsImageModalOpen(false)}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      )}
    </>
  );
};

export default ChatMessage;