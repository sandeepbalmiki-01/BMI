import streamlit as st

import streamlit as st

hide_streamlit_cloud_elements = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    a[title="View source"] {display: none !important;}
    button[kind="icon"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_cloud_elements, unsafe_allow_html=True)

def calculate_bmi(weight, height):
    return weight / (height * height)

def calorie_breakdown(goal):
    if goal == "weight loss":
        return "Calories: 1500-1800/day\nProtein: 40%\nCarbs: 40%\nFats: 20%"
    elif goal == "muscle gain":
        return "Calories: 2500-3000/day\nProtein: 50%\nCarbs: 30%\nFats: 20%"
    elif goal == "maintain":
        return "Calories: 2000-2200/day\nProtein: 30%\nCarbs: 50%\nFats: 20%"
    else:
        return "Unknown goal."

def meal_plan_veg(goal):
    if goal == "weight loss":
        return """
**Breakfast:** Oats with fruits + Green tea  
**Lunch:** Boiled potatoes + Salad + Brown rice  
**Dinner:** Steamed vegetables + Paneer  
**Snacks:** Nuts (almonds/walnuts) + 1 apple
"""
    elif goal == "muscle gain":
        return """
**Breakfast:** Peanut butter + Whole wheat bread + Banana  
**Lunch:** Daal chawal + Curd + Whey  
**Dinner:** Cheese + 4 Chapatis  
**Snacks:** Protein shake + Peanut butter sandwich
"""
    elif goal == "maintain":
        return """
**Breakfast:** Milk + Poha/Upma + Fruit  
**Lunch:** Rajma/Chole + Brown rice + Salad  
**Dinner:** Khichdi + Curd  
**Snacks:** Yogurt + Mixed nuts
"""
    else:
        return "Meal Plan Not Available."
    
def meal_plan_non_veg(goal):
    if goal == "weight loss":
        return """
**Breakfast:** Oats with fruits + Eggs + Juice  
**Lunch:** Grilled chicken salad + Brown rice  
**Dinner:** Steamed chicken + Paneer  
**Snacks:** Nuts (almonds/walnuts) + 1 apple
"""
    elif goal == "muscle gain":
        return """
**Breakfast:** 4 Eggs + Whole wheat bread + Banana  
**Lunch:** Chicken breast + Quinoa + Broccoli  
**Dinner:** Fish or Paneer + Sweet potato  
**Snacks:** Protein shake + Peanut butter sandwich
"""
    elif goal == "maintain":
        return """
**Breakfast:** Milk + Poha/Upma + Fruit  
**Lunch:** Rajma/Chole + Brown rice + Salad  
**Dinner:** Khichdi + Curd  
**Snacks:** Yogurt + Mixed nuts
"""
    else:
        return "Meal Plan Not Available."

def diet_plan_veg(bmi, goal):
    if goal == "weight loss":
        return "Calorie-deficit is must for you: salads, oats, boiled veggies and green tea."
    elif goal == "muscle gain":
        return "You need a high-protein diet: whey-protein, yogurt, paneer, nuts and complex carbs."
    elif goal == "maintain":
        if bmi < 18.5:
            return "For healthy weight gain, eat calorie-rich, nutritious foods."
        elif 18.5 <= bmi < 24.9:
            return "Maintain a balanced diet: fruits, vegetables, whole grains and proteins."
        else:
            return "Eat in moderation—just what is healthy for your body."
    else:
        return "Invalid goal."
    
def diet_plan_non_veg(bmi, goal):
    if goal == "weight loss":
        return "Calorie-deficit is must for you: salads, grilled chicken, boiled eggs and Fish."
    elif goal == "muscle gain":
        return "You need a high-protein diet: chicken, eggs, roasted-chicken, nuts and complex carbs."
    elif goal == "maintain":
        if bmi < 18.5:
            return "For healthy weight gain, eat calorie-rich, nutritious foods."
        elif 18.5 <= bmi < 24.9:
            return "Maintain a balanced diet: fruits, vegetables, whole grains and proteins."
        else:
            return "Eat in moderation—just what is healthy for your body."
    else:
        return "Invalid goal."
    

def main():
    st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                                url("https://images.pexels.com/photos/1229356/pexels-photo-1229356.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    label {
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style="color:SeaShell; text-align:center;">Welcome to Unstoppable</h1>
        <h2 style="color:SeaShell; text-align:center;">Sandeep Balmiki Fitness Guide </h2>
        """,
        unsafe_allow_html=True
    )
  st.markdown(
        """
        <h3 style="color:SeaShell; text-align:center;">About Us</h3>
        <p style="color:SeaShell; text-align:center;">
        At Unstoppable Fitness, we believe in the power of transformation! Whether you're looking to lose weight, gain muscle, or simply maintain a healthy lifestyle, we are here to guide you every step of the way. Our fitness plans are tailored to your individual needs and goals. Join the movement and start your fitness journey with us today!
        </p>
        """,
        unsafe_allow_html=True
    )
    weight = st.number_input("Enter your weight (kg):", min_value=10.0, max_value=185.0, step=0.5,)
    height_cm = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, step=0.5)

    goal = st.selectbox("What is your fitness goal?", ("-select-", "weight loss", "muscle gain", "maintain"))
    cat = st.selectbox("Are you Veg or Non-Veg?", ("-select-", "veg", "non-veg"))

    if st.button("Get Your Diet Plan"):
            if cat == "veg":
                height_m = height_cm / 100
                bmi = calculate_bmi(weight, height_m)

                st.subheader("📊 Your BMI")
                st.write(f"**{bmi:.2f}**")

                st.subheader("🍽️ Diet Advice")
                st.write(diet_plan_veg(bmi, goal))

                st.subheader("🔥 Calorie Breakdown")
                st.text(calorie_breakdown(goal))

                st.subheader("📅 Example Meal Plan")
                st.markdown(meal_plan_veg(goal))

                st.markdown("---")
                st.success("💧 Tip: Regular exercise & hydration are key to a healthy lifestyle!")

            elif cat == "non-veg":
                height_m = height_cm / 100
                bmi = calculate_bmi(weight, height_m)

                st.subheader("📊 Your BMI")
                st.write(f"**{bmi:.2f}**")

                st.subheader("🍽️ Diet Advice")
                st.write(diet_plan_non_veg(bmi, goal))

                st.subheader("🔥 Calorie Breakdown")
                st.text(calorie_breakdown(goal))

                st.subheader("📅 Example Meal Plan")
                st.markdown(meal_plan_non_veg(goal))

                st.markdown("---")
                st.success("💧 Tip: Regular exercise & hydration are key to a healthy lifestyle!\nThanks for visiting  Unstoppable Sandeep Balmiki Fitness Guide")

if __name__ == "__main__":
    main()
