<template>
    <div class="contact-container">
      <div class="contact-content">
        <h1>Contact Us</h1>
        <p>If you have any questions or need further information, feel free to reach out to us using the contact details below.</p>
        <div class="contact-details">
          <div class="detail">
            <i class="fas fa-envelope"></i>
            <span>Email: <a href="mailto:dubeysarthak47@gmail.com">dubeysarthak47@gmail.com</a></span>
          </div>
          <div class="detail">
            <i class="fas fa-phone-alt"></i>
            <span>Phone: <a href="tel:+91-8770210619">+91-8770210619</a></span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ContactUs'
  }
  </script>
  
  <style scoped>
  .contact-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
    color: #fff;
    font-family: 'Poppins', sans-serif;
    text-align: center;
  }
  
  .contact-content {
    padding: 2rem;
    background: rgba(0, 0, 0, 0.6);
    border-radius: 10px;
    max-width: 600px;
    width: 100%;
  }
  
  h1 {
    font-size: 3rem;
    background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
    color: #e0e0e0;
  }
  
  .contact-details {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .detail {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
  }
  
  .detail i {
    font-size: 1.5rem;
    color: #fbd786;
  }
  
  .detail a {
    color: #fbd786;
    text-decoration: none;
  }
  
  .detail a:hover {
    text-decoration: underline;
  }
  
  @media (max-width: 768px) {
    h1 {
      font-size: 2.5rem;
    }
    p {
      font-size: 1rem;
    }
    .detail {
      font-size: 1rem;
    }
  }
  
  @media (max-width: 480px) {
    h1 {
      font-size: 2rem;
    }
    p {
      font-size: 0.9rem;
    }
    .detail {
      font-size: 0.9rem;
    }
  }
  </style>
  