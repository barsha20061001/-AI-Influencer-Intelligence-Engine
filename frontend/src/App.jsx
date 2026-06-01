import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [influencers, setInfluencers] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/influencers")
      .then((res) => setInfluencers(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <h1 className="text-4xl font-bold mb-6">
        Ratefluencer AI Dashboard
      </h1>

      <table className="w-full border border-slate-700">
        <thead>
          <tr className="bg-slate-800">
            <th className="p-3">Username</th>
            <th className="p-3">Followers</th>
            <th className="p-3">Category</th>
          </tr>
        </thead>

        <tbody>
          {influencers.map((i, idx) => (
            <tr key={idx} className="border-t border-slate-700">
              <td className="p-3">{i.username}</td>
              <td className="p-3">{i.followers}</td>
              <td className="p-3">{i.category}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;