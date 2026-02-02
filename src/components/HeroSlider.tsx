import { useState, useEffect } from "react";

interface HeroSliderProps {
  words?: string[];
  interval?: number;
}

const HeroSlider = ({
  words = ["Code.", "Create.", "Conquer.", "Repeat."],
  interval = 1500,
}: HeroSliderProps) => {
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % words.length);
    }, interval);
    return () => clearInterval(timer);
  }, [words, interval]);

  return (
    <div className={"hero-slider"}>
      {words.map((word, index) => (
        <p
          key={index}
          className={`slider-word ${index === current ? "active" : ""}`}
        >
          {word}
        </p>
      ))}
    </div>
  );
};

export default HeroSlider;
