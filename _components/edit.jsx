export default function Header({ title, description }) {
    return (
      <header>
        <h1>title: {title}</h1>
        <p>{description}</p>
      </header>
    );
  }