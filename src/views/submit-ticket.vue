<template>
  <div class="submit-ticket-container">
    <h1 class="submit-ticket-title">Submit Ticket</h1>
    <form @submit.prevent="submitTicket" class="submit-ticket-form">
      <input 
        type="text" 
        v-model="title" 
        placeholder="Title" 
        required 
        class="input-field"
      />
      <textarea 
        v-model="description" 
        placeholder="Description" 
        required 
        class="textarea-field"
      ></textarea>
      <select v-model="category" required class="select-field">
        <option value="" disabled selected>Select Category</option>
        <option value="Cleaning">Cleaning</option>
        <option value="Carpentry">Carpentry</option>
        <option value="Electrical">Electrical</option>
        <option value="Plumbing">Plumbing</option>
      </select>
      <button type="submit" class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      description: '',
      category: ''
    }
  },
  methods: {
    async submitTicket() {
      try {
        console.log(this,localStorage.getItem('token')) ;
        await this.$http.post('/submit-ticket/', {
          title: this.title,
          description: this.description,
          category: this.category
        }, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        })
        this.$router.push('/dashboard')
      } catch (error) {
        console.error('Failed to submit ticket:', error)
      }
    }
  }
}
</script>

<style scoped>
/* Container Styling */
.submit-ticket-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  background: linear-gradient(135deg, #f5f7fa, #e2ebf0);
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Title Styling */
.submit-ticket-title {
  text-align: center;
  font-size: 2rem;
  color: #333;
  margin-bottom: 1.5rem;
  font-family: 'Poppins', sans-serif;
}

/* Form Input Fields */
.input-field, .textarea-field, .select-field {
  width: 100%;
  padding: 1rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  font-family: 'Poppins', sans-serif;
  transition: border-color 0.3s ease;
}

.input-field:focus, .textarea-field:focus, .select-field:focus {
  border-color: #4a90e2;
  outline: none;
}

/* Textarea Field */
.textarea-field {
  height: 150px;
  resize: none;
}

/* Submit Button */
.submit-button {
  width: 100%;
  padding: 1rem;
  background-color: #4a90e2;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-family: 'Poppins', sans-serif;
}

.submit-button:hover {
  background-color: #3a78c0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .submit-ticket-container {
    padding: 1.5rem;
  }

  .submit-ticket-title {
    font-size: 1.75rem;
  }

  .input-field, .textarea-field, .select-field {
    padding: 0.8rem;
    font-size: 0.95rem;
  }

  .submit-button {
    padding: 0.9rem;
    font-size: 1.1rem;
  }
}
</style>
