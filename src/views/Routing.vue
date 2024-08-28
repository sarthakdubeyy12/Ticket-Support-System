<template>
  <div class="routing-container">
    <div class="content">
      <h1>Welcome to the Routing Section!</h1>
      <p>Explore the different routes of our application and discover all the exciting features we offer.</p>
      <div class="buttons">
        <button @click="navigate('home')">Home</button>
        <button @click="navigate('about')">About Us</button>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Routing',
  methods: {
    navigate(route) {
      this.$router.push({ name: route });
    }
  }
}
</script>

<style scoped>
.routing-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #ff6f61 0%, #d966ff 100%);
  color: #fff;
  text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
  font-family: 'Poppins', sans-serif;
  text-align: center;
}

.content {
  padding: 2rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

h1 {
  font-size: 3rem;
  background: linear-gradient(135deg, #fbc2eb 0%, #a18cd1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #e0e0e0;
}

.buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

button {
  background: #ff6f61;
  border: none;
  border-radius: 5px;
  color: #fff;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background: #e55b5b;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }
  p {
    font-size: 1rem;
  }
  button {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 2rem;
  }
  p {
    font-size: 0.9rem;
  }
  button {
    padding: 0.5rem 0.75rem;
    font-size: 0.8rem;
  }
}
</style>
