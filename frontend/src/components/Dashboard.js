import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
  Users, 
  CheckSquare, 
  TrendingUp, 
  Phone, 
  Mail, 
  Calendar,
  ArrowUpRight,
  ArrowDownRight
} from 'lucide-react';
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell
} from 'recharts';
import axios from 'axios';

const COLORS = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'];

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardStats();
  }, []);

  const fetchDashboardStats = async () => {
    try {
      const response = await axios.get('http://localhost:8000/dashboard/stats');
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching dashboard stats:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  const contactStats = [
    {
      name: 'Total Contacts',
      value: stats?.total_contacts || 0,
      icon: Users,
      color: 'text-blue-600',
      bgColor: 'bg-blue-100'
    },
    {
      name: 'Leads',
      value: stats?.total_leads || 0,
      icon: ArrowUpRight,
      color: 'text-green-600',
      bgColor: 'bg-green-100'
    },
    {
      name: 'Prospects',
      value: stats?.total_prospects || 0,
      icon: TrendingUp,
      color: 'text-yellow-600',
      bgColor: 'bg-yellow-100'
    },
    {
      name: 'Customers',
      value: stats?.total_customers || 0,
      icon: ArrowDownRight,
      color: 'text-purple-600',
      bgColor: 'bg-purple-100'
    }
  ];

  const taskStats = [
    {
      name: 'Total Tasks',
      value: stats?.total_tasks || 0,
      icon: CheckSquare,
      color: 'text-indigo-600',
      bgColor: 'bg-indigo-100'
    },
    {
      name: 'Pending',
      value: stats?.pending_tasks || 0,
      icon: Calendar,
      color: 'text-orange-600',
      bgColor: 'bg-orange-100'
    },
    {
      name: 'Completed',
      value: stats?.completed_tasks || 0,
      icon: CheckSquare,
      color: 'text-green-600',
      bgColor: 'bg-green-100'
    }
  ];

  const dealStats = [
    {
      name: 'Total Deals',
      value: stats?.total_deals || 0,
      icon: TrendingUp,
      color: 'text-emerald-600',
      bgColor: 'bg-emerald-100'
    },
    {
      name: 'Deal Value',
      value: `$${(stats?.total_deal_value || 0).toLocaleString()}`,
      icon: TrendingUp,
      color: 'text-emerald-600',
      bgColor: 'bg-emerald-100'
    }
  ];

  const dealsByStage = Object.entries(stats?.deals_by_stage || {}).map(([stage, count]) => ({
    name: stage.replace('_', ' ').toUpperCase(),
    value: count
  }));

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
        <p className="mt-1 text-sm text-gray-500">
          Welcome back! Here's what's happening with your CRM.
        </p>
      </div>

      {/* Contact Stats */}
      <div>
        <h2 className="text-lg font-medium text-gray-900 mb-4">Contacts Overview</h2>
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
          {contactStats.map((stat) => (
            <div key={stat.name} className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className={`p-3 rounded-md ${stat.bgColor}`}>
                      <stat.icon className={`h-6 w-6 ${stat.color}`} />
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">
                        {stat.name}
                      </dt>
                      <dd className="text-lg font-medium text-gray-900">
                        {stat.value}
                      </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Task Stats */}
      <div>
        <h2 className="text-lg font-medium text-gray-900 mb-4">Tasks Overview</h2>
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-3">
          {taskStats.map((stat) => (
            <div key={stat.name} className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className={`p-3 rounded-md ${stat.bgColor}`}>
                      <stat.icon className={`h-6 w-6 ${stat.color}`} />
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">
                        {stat.name}
                      </dt>
                      <dd className="text-lg font-medium text-gray-900">
                        {stat.value}
                      </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Deal Stats */}
      <div>
        <h2 className="text-lg font-medium text-gray-900 mb-4">Deals Overview</h2>
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
          {dealStats.map((stat) => (
            <div key={stat.name} className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className={`p-3 rounded-md ${stat.bgColor}`}>
                      <stat.icon className={`h-6 w-6 ${stat.color}`} />
                    </div>
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">
                        {stat.name}
                      </dt>
                      <dd className="text-lg font-medium text-gray-900">
                        {stat.value}
                      </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Deals by Stage Chart */}
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Deals by Stage</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={dealsByStage}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {dealsByStage.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Recent Interactions */}
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Recent Interactions</h3>
          <div className="space-y-4">
            {stats?.recent_interactions?.slice(0, 5).map((interaction) => (
              <div key={interaction.id} className="flex items-center space-x-3">
                <div className="flex-shrink-0">
                  {interaction.type === 'call' && <Phone className="h-5 w-5 text-blue-500" />}
                  {interaction.type === 'email' && <Mail className="h-5 w-5 text-green-500" />}
                  {interaction.type === 'meeting' && <Calendar className="h-5 w-5 text-purple-500" />}
                  {interaction.type === 'note' && <CheckSquare className="h-5 w-5 text-gray-500" />}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-gray-900 truncate">
                    {interaction.subject}
                  </p>
                  <p className="text-sm text-gray-500">
                    {new Date(interaction.created_at).toLocaleDateString()}
                  </p>
                </div>
              </div>
            ))}
            {(!stats?.recent_interactions || stats.recent_interactions.length === 0) && (
              <p className="text-sm text-gray-500">No recent interactions</p>
            )}
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-medium text-gray-900 mb-4">Quick Actions</h3>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <Link
            to="/contacts"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700"
          >
            <Users className="h-4 w-4 mr-2" />
            Manage Contacts
          </Link>
          <Link
            to="/tasks"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700"
          >
            <CheckSquare className="h-4 w-4 mr-2" />
            View Tasks
          </Link>
          <Link
            to="/deals"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700"
          >
            <TrendingUp className="h-4 w-4 mr-2" />
            Manage Deals
          </Link>
        </div>
      </div>
    </div>
  );
}
