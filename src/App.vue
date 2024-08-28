<template>
  <header>
    <nav class="navbar">
      <div class="navbar-brand">
        <RouterLink to="/" class="brand-link">TicGen</RouterLink>
        <button @click="toggleMenu" class="navbar-burger">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>

      <div :class="{ 'navbar-menu': true, 'is-active': isMenuOpen }">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
        <RouterLink to="/dashboard">Dashboard</RouterLink>
        <RouterLink to="/routing">Routing</RouterLink>
        <RouterLink to="/admin-dashboard">Admin Dashboard</RouterLink>
      </div>
    </nav>
  </header>

  <main class="content">
    <section class="hero-section">
      <h1>Welcome to TicGen</h1>
      <p>Your ultimate platform for seamless ticket management and support solutions.</p>
      <RouterLink to="/login" class="cta-button">Get Started</RouterLink>
    </section>

    <section class="features-section">
      <div class="feature-card">
        <h2>Efficient Support</h2>
        <p>Quickly resolve issues with our streamlined ticketing system.</p>
      </div>
      <div class="feature-card">
        <h2>Admin Dashboard</h2>
        <p>Manage and track tickets efficiently with our powerful dashboard.</p>
      </div>
      <div class="feature-card">
        <h2>User Friendly</h2>
        <p>An intuitive interface that makes managing tickets a breeze.</p>
      </div>
    </section>
  </main>

  <RouterView />
</template>

<style scoped>
/* General Reset and Basic Styling */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
}

/* Navbar Styles with Vibrant Background and Fancy Branding */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #110e0d; /* Vibrant orange background */
  padding: 1px 1px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.brand-link {
  font-size: 2.5rem; /* Increased font size for prominence */
  color: #ffffff;
  text-decoration: none;
  font-weight: bold;
  letter-spacing: 1px;
  background: linear-gradient(45deg, #ffeb3b, #ff5722); /* Gradient text */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: background 0.5s ease;
}

.brand-link:hover {
  background: linear-gradient(45deg, #ff5722, #ffeb3b); /* Reverse gradient on hover */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.navbar-burger {
  display: none;
  flex-direction: column;
  justify-content: space-around;
  width: 24px;
  height: 24px;
  background: transparent;
  border: none;
  cursor: pointer;
}

.navbar-burger span {
  width: 100%;
  height: 2px;
  background-color: #ffffff;
}

.navbar-menu {
  display: flex;
  align-items: center;
}

.navbar-menu a {
  padding: 0.5rem 1rem;
  color: #ffffff;
  text-decoration: none;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.navbar-menu a:hover {
  background-color: #d84315;
  border-radius: 5px;
  color: #ffeb3b;
}

@media (max-width: 768px) {
  .navbar-burger {
    display: flex;
  }

  .navbar-menu {
    display: none;
    flex-direction: column;
    width: 100%;
    background-color: #ff5722;
    padding: 1rem 0;
  }

  .navbar-menu.is-active {
    display: flex;
  }

  .navbar-menu a {
    text-align: center;
    padding: 1rem;
    width: 100%;
  }
}

/* Main content style with Background Image */
main {
  padding-top: 100px; /* Adjusted for smaller screens */
  background: url('path-to-your-image.jpg') no-repeat center center; /* Add your image here */
  background-size: cover;
  padding: 2rem 1rem; /* Reduced padding for better responsiveness */
  min-height: 100vh;
}

/* Hero Section Styles */
.hero-section {
  text-align: center;
  padding: 2rem 1rem;
  background: rgba(74, 144, 226, 0.7); /* Semi-transparent background to ensure text readability */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.hero-section h1 {
  font-size: 2rem; /* Reduced font size for better fit on smaller screens */
  color: #ffffff;
  margin-bottom: 1rem;
}

.hero-section p {
  font-size: 1rem; /* Adjusted font size */
  color: #ffffff;
  margin-bottom: 2rem;
}

.cta-button {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #ffdd57;
  color: #333;
  font-size: 1rem; /* Adjusted font size */
  font-weight: 600;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.cta-button:hover {
  background-color: #f0c14b;
  color: #222;
}

/* Features Section Styles */
.features-section {
  display: flex;
  flex-wrap: wrap; /* Allow wrapping for better responsiveness */
  justify-content: space-between;
  gap: 1rem;
  margin-top: 2rem;
}

.feature-card {
  flex: 1;
  min-width: 250px; /* Ensures cards stay within bounds on small screens */
  background-color: #ffffff;
  border-radius: 10px;
  padding: 1.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.feature-card h2 {
  font-size: 1.5rem; /* Adjusted for better fit on small screens */
  color: #4169e1;
  margin-bottom: 1rem;
}

.feature-card p {
  font-size: 0.9rem; /* Adjusted for better fit on small screens */
  color: #666;
}
</style>
