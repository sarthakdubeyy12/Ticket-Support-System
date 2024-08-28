<template>
  <div class="about">
    <div class="about-content">
      <h1>Welcome to TicGen</h1>
      <p>
        Where customer satisfaction is our top priority. We understand that
        technical issues can be frustrating and time-consuming, which is why
        we've created a streamlined, efficient support system designed to
        address your needs quickly and effectively.
      </p>
      <p>
        At the heart of our platform is a commitment to providing responsive,
        reliable support. Whether you're facing a minor glitch or a more complex
        issue, our user-friendly ticket system allows you to easily report
        problems, track their progress, and stay informed every step of the way.
        Simply log in with your email and password, submit your concern, and
        rest assured that our dedicated support team is on the case.
      </p>
      <p>
        For administrators, our intuitive interface offers a comprehensive
        overview of all submitted tickets, enabling quick and efficient problem
        resolution. We believe in clear communication, so once your issue is
        resolved, you'll receive a personalized email notification from our
        team, ensuring you're always in the loop.
      </p>
      <p>
        At TicGen, we're more than just a support system—we're your partner in
        maintaining a smooth, seamless experience. Our goal is to help you
        navigate any technical challenges with ease, so you can focus on what
        really matters.
      </p>
      <p>
        Thank you for choosing TicGen. We're here to help, every step of the
        way.
      </p>
    </div>
    <div class="contact-section">
      <h2>Contact Us</h2>
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

.about {
  padding: 2rem;
  background: linear-gradient(135deg, #ff8a00, #e52e71);
  color: #ffffff;
  text-align: center;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  font-family: 'Raleway', sans-serif;
}

.about h1 {
  font-family: 'Lobster', cursive;
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #ffd700;
}

.about-content {
  max-width: 800px;
  margin: auto;
  line-height: 1.6;
}

.about p {
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.contact-section {
  margin-top: 2rem;
  background: rgba(0, 0, 0, 0.3);
  padding: 1.5rem;
  border-radius: 10px;
}

.contact-section h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #ffd700;
}

.contact-details {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
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

@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
}
</style>
