<template>
  <div class="login-container">
    <div class="login-card">
      <h1>Login to TicGen</h1>
      <p>Access your dashboard by logging in with your credentials.</p>
      <form @submit.prevent="login">
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <div class="remember-me">
          <input type="checkbox" id="rememberMe" />
          <label for="rememberMe">Remember Me</label>
        </div>
        <button type="submit" class="login-button">Login</button>
      </form>
      <router-link to="/signup" class="signup-link">Don't have an account? Sign Up</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await this.$http.post('/login', {
          email: this.email,
          password: this.password
        })
        localStorage.setItem('token', response.data.access_token || "token")
        this.$router.push('/dashboard')
      } catch (error) {
        console.error('Login failed:', error)
      }
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

/* Login Container */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #4a90e2, #9013fe); /* Vibrant gradient background */
  padding: 2rem;
}

/* Login Card */
.login-card {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 400px;
}

.login-card h1 {
  font-size: 2rem;
  color: #4169e1; /* Royal blue text color */
  margin-bottom: 1rem;
}

.login-card p {
  color: #666;
  margin-bottom: 2rem;
}

.login-card form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.login-card input[type="email"],
.login-card input[type="password"] {
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.login-card input[type="email"]:focus,
.login-card input[type="password"]:focus {
  outline: none;
  border-color: #4169e1;
  box-shadow: 0 0 5px rgba(65, 105, 225, 0.5);
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.login-card button.login-button {
  padding: 0.75rem;
  background-color: #4169e1;
  color: #fff;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-card button.login-button:hover {
  background-color: #2948ab;
}

.signup-link {
  display: block;
  margin-top: 1rem;
  color: #4169e1;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease;
}

.signup-link:hover {
  color: #2948ab;
}
</style>
