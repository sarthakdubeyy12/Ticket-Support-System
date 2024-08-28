<template>
  <div class="dashboard-container">
    <h1 class="dashboard-title">Dashboard</h1>
    <button @click="SubmitTicket" class="submit-ticket-button">Submit Ticket</button>
    <h2 class="tickets-title">Your Tickets</h2>
    <ul class="tickets-list">
      <li v-for="ticket in tickets" :key="ticket._id" class="ticket-item">
        <span class="ticket-title">{{ ticket.title }}</span>
        <span :class="['ticket-status', ticket.status.toLowerCase()]">{{ ticket.status }}</span>
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
    await this.fetchTickets();
  },
  methods: {
    async fetchTickets() {
      try {
        const response = await this.$http.get('/tickets/', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        })
        this.tickets = response.data;
      } catch (error) {
        console.error('Failed to fetch tickets:', error);
      }
    },
    SubmitTicket() {
      this.$router.push('/submit-ticket'); // Navigate to SubmitTicket route
    }
  }
}
</script>

<style scoped>
/* General Reset and Basic Styling */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
}

/* Dashboard Container */
.dashboard-container {
  background-color: #f5f7fa;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 2rem auto;
}

/* Dashboard Title Styling */
.dashboard-title {
  font-size: 2.5rem;
  color: #4169e1;
  text-align: center;
  margin-bottom: 2rem;
}

/* Submit Ticket Button Styling */
.submit-ticket-button {
  display: block;
  width: 100%;
  padding: 0.75rem 1.5rem;
  background-color: #ffdd57;
  color: #333;
  font-size: 1.1rem;
  font-weight: 600;
  text-align: center;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
  margin-bottom: 2rem;
}

.submit-ticket-button:hover {
  background-color: #f0c14b;
  color: #222;
}

/* Tickets Section Title */
.tickets-title {
  font-size: 2rem;
  color: #333;
  margin-bottom: 1.5rem;
  text-align: center;
}

/* Tickets List Styling */
.tickets-list {
  list-style: none;
}

.ticket-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.ticket-item:hover {
  transform: translateY(-5px);
}

/* Ticket Title Styling */
.ticket-title {
  font-size: 1.2rem;
  color: #4169e1;
  font-weight: bold;
}

/* Ticket Status Styling */
.ticket-status {
  padding: 0.5rem 1rem;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: capitalize;
}

.ticket-status.open {
  background-color: #ffdd57;
  color: #333;
}

.ticket-status.closed {
  background-color: #4a90e2;
  color: #ffffff;
}

.ticket-status.pending {
  background-color: #9013fe;
  color: #ffffff;
}
</style>
