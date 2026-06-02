import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [influencers, setInfluencers] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  axios
    .get("https://ai-influencer-intelligence-engine.onrender.com/influencers")
    .then((res) => {
      setInfluencers(res.data);
      setLoading(false);
    })
    .catch((err) => {
      console.log(err);
      setLoading(false);
    });
}, []);
  
const categories = ["All", ...new Set(influencers.map((i) => i.category))];

const filteredInfluencers = influencers
  .filter((i) =>
    i.username.toLowerCase().includes(search.toLowerCase())
  )
  .filter((i) =>
    category === "All" ? true : i.category === category
  )
  .sort((a, b) => b.ratefluencer_score - a.ratefluencer_score);

  
  return (
  <div className="min-h-screen bg-slate-950 text-white p-8">
    <h1 className="text-4xl font-bold mb-2">
      Ratefluencer AI Dashboard
    </h1>

    <p className="text-slate-400 mb-8">
      AI-powered influencer authenticity and ranking system
    </p>

    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <div className="bg-slate-900 border border-slate-700 rounded-xl p-5">
        <p className="text-slate-400">Total Influencers</p>
        <h2 className="text-3xl font-bold">{influencers.length}</h2>
      </div>

      <div className="bg-slate-900 border border-slate-700 rounded-xl p-5">
        <p className="text-slate-400">Categories</p>
        <h2 className="text-3xl font-bold">{new Set(influencers.map(i => i.category)).size}</h2>
      </div>

      <div className="bg-slate-900 border border-slate-700 rounded-xl p-5">
        <p className="text-slate-400">Top Authenticity</p>
        <h2 className="text-3xl font-bold">
          {influencers.length > 0
            ? Math.max(...influencers.map((i) => i.authenticity))
            : 0}
        </h2>
      </div>
    </div>

    <div className="flex flex-col md:flex-row gap-4 mb-6">
      <input
        type="text"
        placeholder="Search influencer..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 w-full md:w-1/2 outline-none"
      />

      <select
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        className="bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 w-full md:w-1/4 outline-none"
      >
        {categories.map((cat, idx) => (
          <option key={idx} value={cat}>
            {cat}
          </option>
        ))}
      </select>
    </div>

    {loading ? (
      <p className="text-slate-400">Loading influencers...</p>
    ) : (
      <table className="w-full border border-slate-700">
        <thead>
          <tr className="bg-slate-800">
            <th className="p-3 text-center">Rank</th>
            <th className="p-3 text-center">Username</th>
            <th className="p-3 text-center">Followers</th>
            <th className="p-3 text-center">Category</th>
            <th className="p-3 text-center">Authenticity Score</th>
            <th className="p-3 text-center">Growth Score</th>
            <th className="p-3 text-center">Best Brand</th>
            <th className="p-3 text-center">Brand Match</th>
            <th className="p-3 text-center">Brand Reason</th>
            <th className="p-3 text-center">ML Prediction</th>
            <th className="p-3 text-center">Ratefluencer Score</th>
            <th className="p-3 text-center">Audience</th>
            <th className="p-3 text-center">Expansion</th>
            
            
            
          </tr>
        </thead>

        <tbody>
          {filteredInfluencers.map((i, idx) => (
            <tr key={idx} className="border-t border-slate-700">
              <td className="p-3 text-center font-bold"> #{idx + 1}</td>
              <td className="p-3 text-center">{i.username}</td>
              <td className="p-3 text-center">{i.followers}</td>
              <td className="p-3 text-center">{i.category}</td>
              <td
  className={`p-3 text-center font-bold ${
    i.authenticity >= 85
      ? "text-green-400"
      : i.authenticity >= 70
      ? "text-yellow-400"
      : "text-red-400"
  }`}
>
  {i.authenticity}
</td>
<td className="p-3 text-center font-bold">{i.growth_score}</td>
<td className="p-3 text-center">{i.best_brand}</td>
<td className="p-3 text-center font-bold">{i.brand_match_score}</td>
<td className="p-3 text-center text-sm text-slate-300">
  {i.brand_reason}
</td>
<td className="p-3 text-center font-bold text-cyan-400">
  {i.ratefluencer_score}%
</td>
<td className="p-3 text-center font-bold text-purple-400">
  {i.ratefluencer_score}
</td>
<td className="p-3 text-center">
  {i.audience_age}, {i.audience_country}
</td>
<td className="p-3 text-center font-bold">
  {i.audience_expansion}
</td>
                
              
            </tr>
          ))}
        </tbody>
      </table>
    )}
  </div>
);
}

export default App;