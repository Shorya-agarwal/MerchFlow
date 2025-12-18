import { useState, useEffect } from 'react';
import axios from 'axios';
import TransactionForm from '../components/TransactionForm';
import TransactionList from '../components/TransactionList';

function App() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchTransactions();
  }, []);

  const fetchTransactions = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/transactions/');
      setTransactions(response.data.reverse()); // Show newest first
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // For the MVP, we will manually update the list when a new item is added
  const handleNewTransaction = (newTx) => {
    setTransactions([newTx, ...transactions]);
  };
  
  return (
    <div className="min-h-screen bg-gray-50 font-sans text-gray-900">
      {/* Navbar */}
      <nav className="bg-blue-700 text-white p-4 shadow-lg">
        <div className="max-w-6xl mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold tracking-tight">SmartFinance <span className="text-blue-200 text-sm font-normal">AI Edition</span></h1>
          <div className="text-sm bg-blue-800 px-3 py-1 rounded-full">Intuit Case Study</div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto p-6 grid grid-cols-1 md:grid-cols-3 gap-8 mt-6">
        
        {/* Left Column: Form */}
        <div className="md:col-span-1">
          <TransactionForm onTransactionAdded={handleNewTransaction} />
          
          <div className="mt-6 bg-blue-50 p-4 rounded-xl border border-blue-100 text-sm text-blue-800">
            <strong>How it works:</strong> Type a description like "Dinner at McDonald's". The AI will automatically categorize it as "Food" or "Dining".
          </div>
        </div>

        {/* Right Column: List */}
        <div className="md:col-span-2">
          <TransactionList transactions={transactions} />
        </div>

      </main>
    </div>
  );
}

export default App;