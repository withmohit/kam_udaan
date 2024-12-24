import React from 'react';
import LeadsList from './LeadsList';
import PendingCalls from './PendingCalls';
import RecentInteractions from './RecentInteractions';
import SearchBar from './SearchBar';

function Dashboard() {
  return (
    <div>
      <SearchBar />
      <LeadsList />
      <PendingCalls />
      <RecentInteractions />
    </div>
  );
}

export default Dashboard;
