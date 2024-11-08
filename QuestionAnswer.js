// src/components/QuestionAnswer.js

import React, { useState } from 'react';
import { askQuestion } from '../api';

function QuestionAnswer() {
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleQuestionChange = (event) => {
        setQuestion(event.target.value);
    };

    const handleAskQuestion = async () => {
        setIsLoading(true);
        try {
            const response = await askQuestion(question);
            setAnswer(response.answer);
        } catch (error) {
            console.error('Error fetching answer:', error);
            setAnswer('Error fetching answer. Please try again.');
        }
        setIsLoading(false);
    };

    return (
        <div>
            <h2>Ask a Question</h2>
            <input
                type="text"
                value={question}
                onChange={handleQuestionChange}
                placeholder="Enter your question"
            />
            <button onClick={handleAskQuestion} disabled={isLoading}>
                {isLoading ? 'Processing...' : 'Ask'}
            </button>
            {answer && (
                <div>
                    <h3>Answer:</h3>
                    <p>{answer}</p>
                </div>
            )}
        </div>
    );
}

export default QuestionAnswer;
