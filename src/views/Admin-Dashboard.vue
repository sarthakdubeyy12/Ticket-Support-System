<template>
  <div class="dashboard">
    <h1 class="title">Admin Dashboard</h1>
    <h2 class="subtitle">All Tickets</h2>
    <ul class="ticket-list">
      <li v-for="ticket in tickets" :key="ticket._id" class="ticket-item">
        <div class="ticket-details">
          <span class="ticket-title">{{ ticket.title }}</span> - 
          <span :class="{'status-resolved': ticket.status === 'Resolved', 'status-pending': ticket.status !== 'Resolved'}">
            {{ ticket.status }}
          </span>
        </div>
        <button class="resolve-button" @click="resolveTicket(ticket._id)">Resolve</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tickets: []
    }
  },
  async mounted() {
    try {
      const response = await this.$http.get('/admin/tickets/', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      })
      this.tickets = response.data
    } catch (error) {
      console.error('Failed to fetch tickets:', error)
    }
  },
  methods: {
    async resolveTicket(ticketId) {
      try {
        await this.$http.put(`/admin/tickets/${ticketId}/resolve`, {}, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        })
        this.tickets = this.tickets.map(ticket => ticket._id === ticketId ? { ...ticket, status: 'Resolved' } : ticket)
      } catch (error) {
        console.error('Failed to resolve ticket:', error)
      }
    }
  }
}
</script>

<style scoped>
.dashboard {
  background-color: #f4f4f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
  color: #2c3e50;
  font-size: 2em;
  margin-bottom: 10px;
}

.subtitle {
  color: #3498db;
  font-size: 1.5em;
  margin-bottom: 20px;
}

.ticket-list {
  list-style-type: none;
  padding: 0;
}

.ticket-item {
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-bottom: 10px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.ticket-details {
  display: flex;
  align-items: center;
}

.ticket-title {
  font-weight: bold;
  margin-right: 10px;
}

.status-resolved {
  color: #2ecc71;
}

.status-pending {
  color: #e74c3c;
}

.resolve-button {
  background-color: #3498db;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.resolve-button:hover {
  background-color: #2980b9;
}
</style>
